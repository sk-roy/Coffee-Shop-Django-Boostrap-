from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact, Order
from django.contrib import messages
# Create your views here.

def index(request):
    # messages.success(request, "Waw! This is the Home Page")
    return render(request, 'index.html')
    # return HttpResponse('This is Home Page')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        coffeeName = request.POST.get('coffeeName')
        order = Order(name=name, email=email, phone=phone, coffeeName=coffeeName, data=datetime.today())
        order.save()
        messages.success(request, 'Your Order is comfirmed. Use your name and email to get delivery. Thank You')

    return render(request, 'order.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')

    return render(request, 'contact.html')