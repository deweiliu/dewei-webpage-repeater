from django.urls import path

from repeater.views import controller

urlpatterns = [
    path('', controller.controller, name='repeat'),
]