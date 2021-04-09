from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesFrom
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'database/news_home.html', {'news': news})
# Create your views here.


class NewsDetailView(DetailView):
    model = Articles
    templates_name = 'database/details_views.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    templates_name = 'database/create.html'

    form_class = ArticlesFrom


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    templates_name = 'database/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesFrom()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'database/create.html', data)
