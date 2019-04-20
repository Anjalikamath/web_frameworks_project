from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.homePg, name='homePg'),
    url(r'^blo/contacts',views.contact,name='contact'),
    url(r'^blo/books',views.books,name='books'),
    url(r'^blo/homePg',views.homePg,name='homePg'),
    url(r'^blo/Fiction',views.fiction,name='fiction'),
    url(r'^blo/NonFiction',views.nonfiction,name='nonfiction'),
    url(r'^blo/Education',views.education,name='education'),
]
