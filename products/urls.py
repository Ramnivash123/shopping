from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.products),
    path('products/<str:category>/', views.products),
    path('addcart/', views.addcart),
    path('viewcart/', views.viewcart),
    path('deletecart/<int:id>/', views.deletecart),
    path('checkout/', views.checkout),
    path('orders/', views.orders),
]