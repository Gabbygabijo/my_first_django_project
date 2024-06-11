from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home),
    path('hello/', views.say_hello),
    path('books/', views.list_of_books),
    path('books/<int:id>', views.book_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)