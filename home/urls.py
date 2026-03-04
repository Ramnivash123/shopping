from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup),
    path('signin/', views.signin),
    path('admin_dash/', views.admin_dash),
    path('user_dash/', views.user_dash),
    path('signout/', views.signout),
    path('edit/<int:id>/', views.edit),
    path('edited/<int:id>/', views.edited),
    path('delete/<int:id>/', views.delete),
]