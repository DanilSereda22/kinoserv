from django.urls import path
from django.urls import re_path
from firstapp import views
urlpatterns = [
re_path (r'^about/contact/', views.contact),
re_path(r'^about', views.about),
path ("", views. index),
]

