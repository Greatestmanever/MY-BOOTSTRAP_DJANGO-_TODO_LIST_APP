from django.urls import path
from todo import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('confirm_delete/<str:pk>/', views.confirm_delete, name="confirm_delete"),

]
