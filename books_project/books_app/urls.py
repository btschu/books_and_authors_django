from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books/<int:id>', views.one_book),
    path('authors/<int:id>', views.one_author),
]
