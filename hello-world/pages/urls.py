from . import views
from django.urls import path

urlpatterns = [
    path('', views.homePageView, name='home')
]
