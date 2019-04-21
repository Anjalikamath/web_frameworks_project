from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as as_views
#from accounts import views as view
#from mysite.core import views as core_views
#from django.contrib.auth import views
urlpatterns = [
    path('', views.homePg, name='homePg'),
    url(r'^blo/contacts',views.contact,name='contact'),
    url(r'^blo/books',views.books,name='books'),
    url(r'^blo/homePg',views.homePg,name='homePg'),
    url(r'^blo/homepg2',views.homepg2,name='homepg2'),
    url(r'^blo/Fiction',views.fiction,name='fiction'),
    url(r'^blo/NonFiction',views.nonfiction,name='nonfiction'),
    url(r'^blo/Education',views.education,name='education'),
    url(r'^registration/login', as_views.LoginView.as_view(), name='login.html'),
    url(r'^registration/logout', as_views.LogoutView.as_view(), name='logout.html'),
    url(r'^blo/signup',views.SignUp.as_view(),name='signup'),
    #url(r'^login/$', views.login, name='login.html'),
    #url(r'^logout/$', views.logout, name='logout.html'),

    #url(r'^blo/registeration',views.registeration,name='registeration'),
    #url(r'^blo/login',views.user_login,name='user_login'),
]
