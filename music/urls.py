from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('nuty/', views.music_notes, name='music_notes'),
    path('nuty/dodaj/', views.add_music_notes, name='add_music_notes'),
    path('nuty/<int:pk>/', views.music_notes_details, name='music_notes_details'),
    path('nuty/usun/<int:pk>/', views.delete_music_notes, name='delete_music_notes'),
    path('nuty/dodaj/<int:pk>/', views.edit_music_notes, name='edit_music_notes')
]
