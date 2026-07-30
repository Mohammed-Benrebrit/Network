from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    numfollowers = models.IntegerField(default=0)
    numfollowing = models.IntegerField(default=0)


class post(models.Model):
    id = models.AutoField(primary_key=True)
    postfk = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    numoflikes = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)


class followers(models.Model):

    acc = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="account")
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower")


class following(models.Model):

    acc = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="faccount")
    follow = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follow")


class likes(models.Model):
    likedpost = models.ForeignKey(
        post, on_delete=models.CASCADE, related_name="likedpost")
    userlike = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userlike")
