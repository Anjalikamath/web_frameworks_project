from django.shortcuts import render
from .models import Books
# Create your views here.
def post_list(request):
    posts=Books.objects.all()
    return render(request,'blo/homepg.html',{'posts':posts})
