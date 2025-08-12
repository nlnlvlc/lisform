from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="form"),
    path('success/', views.display_saved_data, name="success")
]