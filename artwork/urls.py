from django.urls import path, include
from . import views

urlpatterns = [
    path('timeline/', views.timeline, name="timeline"),
    path('upload', views.upload, name="upload")
    
]
