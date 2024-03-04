from django.shortcuts import render, redirect
from . import models

def index_page(request):
    return render(request,'index.html')


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request,'contact.html')


def login_page(request):
    a = models.Contact.objects.all()
    context = {'form': a}
    if request.method == 'POST':
        x = models.Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            contact=request.POST.get('contact'),
             )
        if x is not None:
            x.save()
            return redirect('/')
    return render(request,'login.html')


def buy_page(request):
    return render(request, 'buy.html')
