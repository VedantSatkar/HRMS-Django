from django.urls import path
from . import views

app_name = 'notification'

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('add/', views.add_notification, name='add_notification'),
    path('edit/<int:notification_id>/', views.edit_notification, name='edit_notification'),
    path('delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
]
