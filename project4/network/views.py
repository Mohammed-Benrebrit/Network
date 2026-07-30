from codecs import latin_1_decode
import json
from pyexpat import model
from re import U
import re
from turtle import pos
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from .models import *


def index(request):
    if request.method == "POST":
        np = request.POST["po"]
        postt = post()
        postt.text = np
        postt.postfk = request.user
        postt.save()
        posts = post.objects.all().order_by("-id")
        return render(request, "network/index.html", {
            "posts": posts
        })

    else:
        userposts = post.objects.filter().order_by("-id")
        pag = Paginator(userposts, 10)
        page_number = request.GET.get('page')
        page_obj = pag.get_page(page_number)

        return render(request, "network/index.html", {
            "posts": page_obj
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required(login_url='/login')
@csrf_exempt
def profile(request, uname):
    if request.method == "POST":
        data = json.loads(request.body)
        usns = [i.strip() for i in data.get("usn").split(",")]
        l = usns[0]
        s = User.objects.get(username=l)
        nmg = User.objects.get(username=request.user)
        ch = data.get("check")

        if ch == 't':
            # adding the account that has ben followed to the this acoount
            flwing = following()
            flwing.acc = request.user
            flwing.follow = s
            nmg.numfollowing += 1
            nmg.save()
            flwing.save()

            # adding the new follwer to the account that has ben followed
            flwrs = followers()
            flwrs.acc = s
            flwrs.follower = request.user
            s.numfollowers += 1
            s.save()
            flwrs.save()
        elif ch == 'f':
            # delete the following
            fling = following.objects.filter(acc=request.user, follow=s)
            fling.delete()
            nmg.numfollowing -= 1
            nmg.save()

            # delete the follower
            flrs = followers.objects.filter(acc=s, follower=request.user)
            flrs.delete()
            s.numfollowers -= 1
            s.save()

        # showing followers and following

        return JsonResponse({"message": ch}, status=201)
    elif request.method == "PUT":
        data = json.loads(request.body)
        postid = data.get("pid")
        newtext = data.get('ntx')

        modpost = post.objects.get(id=postid)
        modpost.text = newtext
        modpost.save()

        return JsonResponse({"message": 'post Edited'}, status=201)
    else:
        us = uname
        userdata = User.objects.filter(username=us)
        for i in userdata:
            us = i.id
        check = following
        try:
            check = following.objects.get(acc=request.user, follow=us)
        except check.DoesNotExist:
            check = None
        userposts = post.objects.filter(postfk=us).order_by("-id")
        pag = Paginator(userposts, 10)
        page_number = request.GET.get('page')
        page_obj = pag.get_page(page_number)

        return render(request, "network/profile.html", {
            "udata": userdata,
            "posts": page_obj,
            "check": check
        })


@login_required(login_url='/login')
@csrf_exempt
def followings(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        postid = data.get("pid")
        lpost = post.objects.get(id=postid)
        check = likes.objects.filter(likedpost=lpost, userlike=request.user)

        if len(check) == 0:
            like = likes()
            like.likedpost = lpost
            like.userlike = request.user
            like.save()
            lpost.numoflikes += 1
            lpost.save()
        else:
            check = likes.objects.get(likedpost=lpost, userlike=request.user)
            check.delete()
            lpost.numoflikes -= 1
            lpost.save()
        return JsonResponse({"message": postid}, status=201)

    else:
        find = User.objects.get(username=request.user)
        accounts = following.objects.filter(acc=find.id)
        check = likes.objects.filter(userlike=request.user)

        data = post.objects.filter(
            postfk__in=User.objects.filter(follow__in=accounts)).order_by("-id").prefetch_related('likedpost')

        pag = Paginator(data, 10)
        page_number = request.GET.get('page')
        page_obj = pag.get_page(page_number)

        return render(request, "network/followings.html", {
            "posts": page_obj,
            "check": check
        })
