from django.urls import path
from . import views

app_name = 'performance'

urlpatterns = [
    path('', views.performance_list, name='performance_list'),
    path('add/', views.add_performance, name='add_performance'),
    path('edit/<int:performance_id>/', views.edit_performance, name='edit_performance'),
    path('delete/<int:performance_id>/', views.delete_performance, name='delete_performance'),
]
