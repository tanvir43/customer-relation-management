from django.urls import path
from .views import customers

urlpatterns = [
    path('', customers, name='customers'),
]