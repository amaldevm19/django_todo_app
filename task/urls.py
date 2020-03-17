from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'list'),
    path('edit/<str:pk>/', views.editTask, name='edit'),
    path('delete/<str:pk>/', views.deleteTask, name='delete')
]