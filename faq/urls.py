from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_faq, name='all_faq'),
    path('add_question/', views.add_question, name='add_question'),
    path('edit_question/<int:faq_id>/', views.edit_question, name='edit_question'),
    path('delete_question/<int:faq_id>/', views.delete_question, name='delete_question'),
]
