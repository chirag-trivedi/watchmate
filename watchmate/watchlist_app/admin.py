from django.contrib import admin
from django.db import models
from watchlist_app.models import WatchList,StreamPlatform

# Register your models here.

admin.site.register(WatchList)
admin.site.register(StreamPlatform)