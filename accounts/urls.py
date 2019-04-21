'''
from django.urls import path
from django.conf.urls import url

from . import views
#from accounts.views import SignUp

'''
urlpatterns = [
    path('blo/signup/', SignUp.as_view(), name='signup'),
    #url(r'/signup',SignUp.as_view(),name='signup'),
]
'''

urlpatterns = [
    url(r'^blo/signup', views.SignUp.as_view(), name='signup'),
    #url(r'^blo/signup',view.SignUp,name='signup'),
]
'''
