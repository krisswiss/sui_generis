from django.urls import path
from . import views

urlpatterns = [
    path('', views.Faq, name='Faq'),
]
