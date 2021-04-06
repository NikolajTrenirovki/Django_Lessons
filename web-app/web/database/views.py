from django.shortcuts import render


def news_home(request):
    return render(request, 'database/news_home.html')
# Create your views here.
