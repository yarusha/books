from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about, name='about'),
    path('book/<int:id>/view/', views.book_view, name='book_view'),
    path('book/<int:id>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:id>/delete/', views.book_delete, name='book_delete'),
]