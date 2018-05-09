from django.shortcuts import render
from polls import models


def home(request):
    string = "123"
    return render(request, 'home.html', {'data': string})

def textpost(request):
    name = request.POST['name']
    content = request.POST['content']
    models.Article.objects.create(title=name,content=content)
    return render(request, 'home.html', {'data': name})

def lyb(request):
    string = models.Article.objects.all()
    return render(request, 'lyb.html', {'data': string})
