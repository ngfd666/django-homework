from django.urls import path

from . import views

urlpatterns = [
    path('', views.save_note),
    path('delete_note/', views.delete_note),
    path('notes/', views.note_list),
    path('notes/<int:pk>/', views.note_detail),
]
