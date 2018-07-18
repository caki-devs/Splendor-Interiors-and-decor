from django.conf.urls import url
from . import views

urlpatterns=[
    url('index.html', views.home, name='home'),
    url('shop.html', views.shop, name='shop'),
    url('services.html', views.services, name='services'),
    url('cart.html', views.cart, name='cart'),
    url('product-details.html', views.product, name='product'),
    url('404.html', views.fourowfour, name='fourowfour'),
    url('checkout.html', views.checkout, name='checkout')
]