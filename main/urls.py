from django.urls import path
from .views import home, categories, product_details, contact

urlpatterns = [
    path('', home),
    path('categories/', categories),
    path('product-details/', product_details),
    path('contact/', contact),
]