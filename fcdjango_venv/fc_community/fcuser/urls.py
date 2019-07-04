from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.regitser),
    path('login/', views.login),
    path('logout/', views.logout),
    path('', views.home)
]
