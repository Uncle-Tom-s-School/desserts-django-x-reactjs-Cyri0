from django.urls import path
from . import views

urlpatterns = [
    path('desserts/', views.getDesserts, name="getDesserts")
]
