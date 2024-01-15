from .import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='index'),
    path('contact/', views.contact,name='contact')
]
