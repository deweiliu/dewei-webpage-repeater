from django.urls import path

from repeater.views.repeat import repeat
from repeater.views import home

urlpatterns = [
    path('', repeat.repeat, name='repeat'),
]