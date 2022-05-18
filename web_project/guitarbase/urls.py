from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='guitarbase-home'),
    path('delete_artist/<str:pk>/', views.delete_artist, name='guitarbase-delete-artist'),
    path('delete_song/<str:pk>/', views.delete_song, name='guitarbase-delete-song')
]
