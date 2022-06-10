from django.urls import path

from .views import someone


urlpatterns = [
    path('', someone, name='home')
]
