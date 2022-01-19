from django.shortcuts import render
from django.http import HttpResponse

def users_views(request):
    return HttpResponse("page d'utilisateur")
