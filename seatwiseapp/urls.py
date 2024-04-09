from django import urls
from .views import *
from .forms import *
from django.urls import path

urlpatterns = [
    path('index/',index),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('moviecards/',moviecard),
    path('cardupload/',cardupload),
    path('carddisplay/',carddisplay),
    path('movieview/<int:id>',movie),
    path('seatsel/<int:id>',seat),
    path('ticket/<int:id>',ticket),
    path('payment/',payment),
    path('test/',test),
    path('delete/<int:id>',cancel)
]