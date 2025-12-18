from django.urls import path
from . import views

app_name = 'recruitment'

urlpatterns = [
    path('', views.recruitment_list, name='recruitment_list'),
    path('add/', views.add_recruitment, name='add_recruitment'),
    path('edit/<int:recruitment_id>/', views.edit_recruitment, name='edit_recruitment'),
    path('delete/<int:recruitment_id>/', views.delete_recruitment, name='delete_recruitment'),
]
