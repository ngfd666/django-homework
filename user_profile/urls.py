from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout),
    path('register/', views.register, name="register"),
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
]
