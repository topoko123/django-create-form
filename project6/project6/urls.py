from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('chrfield/', views.chrfield),
    path('number/', views.number),
    path('email-url/', views.email_url),
    path('boolean/', views.boolean),
    path('choice/', views.choice),
]
