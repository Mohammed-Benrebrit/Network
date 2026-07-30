from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(post)
admin.site.register(followers)
admin.site.register(following)
admin.site.register(likes)
