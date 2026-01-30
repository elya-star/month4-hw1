from django.shortcuts import render
from django.http import HttpResponse

def favorite_quote_view(request):
    if request.method == 'GET':
        return HttpResponse("А судьи кто?")
