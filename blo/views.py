from django.shortcuts import render
from .models import Books
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def homePg(request):
    #posts=Books.objects.all()
    return render(request,'blo/homepg.html',{})
def homepg2(request):
    #posts=Books.objects.all()
    return render(request,'blo/homepg2.html',{})
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

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blo/signup.html'


'''def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/blo/homepg2.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    return render(request,'blo/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def registerion(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'blo/registration.html',{})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'blo/login.html', {})
'''
