from django.shortcuts import render, redirect
from .models import Data

def index(request):

    context = {}
    context['dataset'] = Data.objects.all()
    return render(request,'index/home.html',context)
def index_column(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        money = request.POST.get('money')
        Data.objects.create(name=name,money=money)
        return redirect('index')
    return render(request,'index/home.html')


def calendar(request):
    return render (request, 'index/calendar.html' )
def testing(request):
    if request.method == "POST":
        name = request.POST.get('name')
        money = request.POST.get('money')
        Data.objects.create(name=name, money=money)
        return redirect ('testing')
    return render(request,'index/testing.html')



