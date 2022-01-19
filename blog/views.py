from django.http import HttpResponse
from django.shortcuts import render
from .db_article import articles


def home_view(request):
#return HttpResponse("je suis la page principale")
    return render(request,'home.html')

def contact_view(request):
   #return HttpResponse("Contactez nous sur la page actuelle")
   return render(request,'contact.html')

def article_view(request):
    return render(request,'article.html',context={'articles': articles})

