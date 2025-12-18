from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('download/<int:id>/', views.download_employee, name='download_employee'),
    path('download-all/', views.download_all_employees, name='download_all_employees'),
]
