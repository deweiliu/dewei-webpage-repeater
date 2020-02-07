from django.urls import path

from repeater.views.repeat import repeat

urlpatterns = [
    path('', repeat.repeat, name='repeat'),
]