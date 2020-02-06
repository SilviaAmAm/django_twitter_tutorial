from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse

from mytweets.forms import TweetForm
from mytweets.models import Tweet
from mytweets.models import HashTag
from user_profile.models import User


# Function based view
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('I am called from a GET request!')
#     elif request.method == 'POST':
#         return HttpResponse('I am called from a POST request!')


# Class based view
class Index(View):
    def get(self, request):
        params = {}
        params['name'] = 'Django'
        return render(request, 'base.html', params)

    def post(self, request):
        return HttpResponse('I am called from a POST request!')


class Profile(View):
    """
    Page where you are able to submit a new tweet.
    """

    form_class = TweetForm
    template_name = 'profile.html'

    def get(self, request, username):
        params = {}
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        form = self.form_class(initial={'country':'Netherlands'})

        params['user'] = user
        params['tweets'] = tweets
        params['form'] = form

        return render(request, self.template_name, params)

    def post(self, request, username):

        form = self.form_class(request.POST)

        if form.is_valid():
            user = User.objects.get(username=username)

            tweet = Tweet(
                text=form.cleaned_data['text'],
                user=user,
                country=form.cleaned_data['country'],
            )

            tweet.save()

            words = form.cleaned_data['text'].split(" ")

            for word in words:
                if word[0] == "#":
                    hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.tweet.add(tweet)

            return HttpResponseRedirect(reverse('user-profile', args=[str(user.username)]))

        return render(request, self.template_name, {'form': form})


class HashTagCloud(View):
    """
    Page that shows all the available hashtags
    """

    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params['tweets'] = hashtag.tweet

        return render(request, 'hashtag.html', params)
