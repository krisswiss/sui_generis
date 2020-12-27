from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_faq, name='all_faq'),
    path('edit_question/<int:faq_id>/', views.edit_question, name='edit_question'),
]
