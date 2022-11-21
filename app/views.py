#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        #'Показать текущее время': reverse('current_time'),
        #'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)
#def home_view(request):
    #home = name: 'home_list'
    #home = HomeForm()
    #context = {form: home}
    #return render(request, 'app/home.html', context)


#def home_view(request):
    #template_name = 'templates/app/home.html'
    #pages = {
        #'Главная страница': reverse('home'),
        #'Показать текущее время': ('current_time')
    #}
   # return HttpResponse('Здесь будет сайт!')

def time_view(request):
    current_time = None
    msg = f'Текущее время : {current_time}'
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')

def workdir_view(request):
    return HttpResponse(f'Директория = {os.listdir()}')
