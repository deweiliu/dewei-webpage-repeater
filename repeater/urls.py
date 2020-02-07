from django.urls import path

from repeater.views.repeat import repeat
from repeater.views import home

urlpatterns = [
    path('<path:encoded_url>', repeat.repeat, name='repeat'),
    path('', home.home, name='home'),
]