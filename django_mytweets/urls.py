"""django_mytweets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from mytweets.views import Profile
from mytweets.views import Index
from mytweets.views import HashTagCloud
from mytweets.views import Search
from mytweets.views import TweetDetails


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Index.as_view(), name='index'),
    path('user/<username>/', Profile.as_view(), name='user-profile'),
    path('user/<username>/<int:pk>/', TweetDetails.as_view(), name='tweet-detail'),
    path('hashtag/<hashtag>/', HashTagCloud.as_view(), name='hashtag'),
    path('search/', Search.as_view(), name='search')
]
