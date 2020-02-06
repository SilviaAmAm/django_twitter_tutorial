from django.contrib import admin

from mytweets.models import Tweet
from mytweets.models import HashTag

admin.site.register(Tweet)
admin.site.register(HashTag)
