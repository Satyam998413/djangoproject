from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from home.models import Accounts
from django.contrib import messages

# Create your views here.
def index(request):
    # # return HttpResponse("raja is the king"
      
    return render(request, 'index.html')


def videos(request):
    return render(request,"videos.html")

def mechanical(request):
    return render(request,"mechanical.html")

def electrical(request):
    return render(request,"electrical.html")

def cs(request):
    return render(request,"cs.html")

def civil(request):
    return render(request,"civil.html")


def accounts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today(),password=password)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'accounts.html')

