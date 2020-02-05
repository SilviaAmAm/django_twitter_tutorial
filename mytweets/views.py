from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


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

