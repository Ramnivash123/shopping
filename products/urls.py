from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('products/', views.products),
    path('products/<str:category>/', views.products),
    path('addcart/', views.addcart),
    path('viewcart/', views.viewcart),
    path('deletecart/<int:id>/', views.deletecart),
    path('checkout/', views.checkout),
    path('orders/', views.orders),
    path('changepic/<int:id>', views.changepic),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)