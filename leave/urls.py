from django.urls import path
from . import views

app_name = 'leave'

urlpatterns = [
    path('', views.leave_list, name='leave_list'),
    path('add/', views.add_leave, name='add_leave'),
    path('edit/<int:leave_id>/', views.edit_leave, name='edit_leave'),
    path('delete/<int:leave_id>/', views.delete_leave, name='delete_leave'),
]
