from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('login/', views.login),
    path('signup/', views.signup),
    path('tagpost/', views.tagpost),
    path('tagpost/<int:id>', views.tag_detail)
]