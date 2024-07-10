from django.urls import path
from . import views
urlpatterns = [
    path('shop/', views.index, name="Shop Home"),
    path('about/', views.about, name="About Us"),
    path('contact/', views.contact, name="Contact Us"),
    path('tracker/', views.tracker, name="Track Orders"),
    path('search/', views.search, name="Search"),
    path("shop/products/<int:myid>/", views.productview, name="Product View"),
    path('checkout/', views.checkout, name="Checkout"),
]
