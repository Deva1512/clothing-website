from django.shortcuts import render, redirect


def index_page(request):
    return render(request,'index.html')


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request,'contact.html')
