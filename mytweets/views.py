from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic import DetailView
from django.urls import reverse
from django.http import JsonResponse
import json

from mytweets.forms import TweetForm
from mytweets.forms import SearchForm
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


class TweetDetails(View):

    form_class = TweetForm
    template_name = 'tweet_detail.html'

    def get(self, request, username, pk):

        try:
            user = User.objects.get(username=username)
            tweet = Tweet.objects.get(user=user, id=pk)
        except Tweet.DoesNotExist:
            return render(request, self.template_name)

        form = self.form_class(initial={'country': tweet.country, 'text': tweet.text})
        context = {'form': form}

        return render(request, self.template_name, context=context)

    def post(self, request, username, pk):

        form = self.form_class(request.POST)

        if form.is_valid():

            new_text = form.cleaned_data['text']
            user = User.objects.get(username=username)
            tweet = Tweet.objects.get(user=user, id=pk)
            tweet.text = new_text
            tweet.save()

            return HttpResponseRedirect(reverse('user-profile', args=[str(user.username)]))

        context = {'form': form}

        render(request, self.template_name, context=context)


class HashTagCloud(View):
    """
    Page that shows all the available hashtags
    """

    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params['tweets'] = hashtag.tweet

        return render(request, 'hashtag.html', params)


class Search(View):
    """
    Search all the tweets with query
    """

    def get(self, request):
        form = SearchForm()
        params = dict()
        params['search'] = form

        if request.is_ajax():
            query = request.GET.get("query")
            tweets = Tweet.objects.filter(text__icontains=query)
            context = {'tweets': tweets}
            html = render_to_string('partials/_tweet_search.html', context=context)
            data = {"search_results_html": html}
            return JsonResponse(data=data, safe=False)
        else:
            return render(request, 'search.html', params)

    # def post(self, request):
    #     form = SearchForm(request.POST)
    #
    #     if form.is_valid():
    #         query = form.cleaned_data['query']
    #         tweets = Tweet.objects.filter(text__icontains=query)
    #         context = {'query': query, 'tweets': tweets}
    #         return_str = render_to_string('partials/_tweet_search.html', context)
    #
    #         return HttpResponse(json.dumps(return_str), content_type="application/json")
    #     else:
    #         HttpResponseRedirect(reverse('search'))





