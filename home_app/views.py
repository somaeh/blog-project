from django.shortcuts import render,HttpResponse

from blog_app.models import Article

from django.urls import reverse


def home(request):
    articles=Article.objects.all()  #read
    recent_articles=Article.objects.all().order_by('-created')                                                                                                                                                                                                         
   
    return render(request, 'home_app/index.html', {'articles':articles, 'recent_articles': recent_articles,  "name": "salam"})


