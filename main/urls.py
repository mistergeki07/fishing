from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.login),
    path('haha', views.haha, name='haha'),
]
    