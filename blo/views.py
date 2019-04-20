from django.shortcuts import render
from .models import Books
# Create your views here.
def homePg(request):
    #posts=Books.objects.all()
    return render(request,'blo/homepg.html',{})
def contact(request):
    return render(request,'blo/contacts.html',{})
def books(request):
    return render(request,'blo/books.html',{})
#def homePage(request):
    return render(request,'blo/homepg.html',{})
def fiction(request):
    return render(request,'blo/Fiction.html',{})
def nonfiction(request):
    return render(request,'blo/NonFiction.html',{})
def education(request):
    return render(request,'blo/Education.html',{})
