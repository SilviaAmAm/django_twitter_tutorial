from django.shortcuts import render
from django.views.generic import View

from user_profile.models import User
from mytweets.models import Tweet

class Profile(View):
    """
    View to display a user profile
    """

    def get(self, request, pk):
        params = {}
        user = User.objects.get(username=pk)
        tweets = Tweet.objects.filter(user=user)
        params['user'] = user
        params['tweets'] = tweets

        return render(request, 'profile.html', params)
