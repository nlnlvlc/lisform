from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('form/success.html', views.display_saved_data)
]