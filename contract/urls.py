from django.urls import path
from . import views

app_name = 'contract'

urlpatterns = [
    path('', views.contract_list, name='contract_list'),
    path('add/', views.add_contract, name='add_contract'),
    path('edit/<int:contract_id>/', views.edit_contract, name='edit_contract'),
    path('delete/<int:contract_id>/', views.delete_contract, name='delete_contract'),
]
