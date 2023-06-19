from django.urls import path
from . import views

urlpatterns = [
    path('create_authors/', views.create_authors, name='create_authors'),
    path('create_publishers/', views.create_publishers, name='create_publishers'),
    path('create_libraries/', views.create_libraries, name='create_libraries'),
    path('create_books/', views.create_books, name='create_books'),
    path('create_users/', views.create_users, name='create_users'),
    path('create_reviews/', views.create_reviews, name='create_reviews'),
]