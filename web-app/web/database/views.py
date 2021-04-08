from django.shortcuts import render
from .models import Articles
from .forms import ArticlesFrom


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'database/news_home.html', {'news': news})
# Create your views here.


def create(request):
    form = ArticlesFrom()

    data = {
        'form': form
    }

    return render(request, 'database/create.html', data)
