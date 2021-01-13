from django.urls import path
from .views import main_info

urlpatterns = [
    path('', main_info, name='main_info'),
]
