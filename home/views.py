from django.shortcuts import render,HttpResponse
from home.models import Contact,about1

# Create your views here.
def index(Request):
     if Request.method == "POST":
          Name = Request.POST.get('Name')
          Email = Request.POST.get('Email')
          Phone = Request.POST.get('Phone')
          contact = Contact(Name=Name,Email=Email,Phone=Phone)
          contact.save()
     return render(Request , 'index.html')
def about(Request):
     if Request.method == "POST":
          Name = Request.POST.get('name')    
          Email = Request.POST.get('Email')    
          Phone = Request.POST.get('Phone')
          About = about1(Name=Name,Email=Email,Phone=Phone)
          About.save() 
     return render(Request,'contact.html')