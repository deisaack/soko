from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create-product/$', views.ProductCreateView.as_view(), name='product_create'),
    url(r'^$', views.ProductListView.as_view(), name='product_list'),
    url(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^cart/(?P<pk>\d+)/$', views.CartDetailView.as_view(), name='cart_detail'),
    url(r'^cart/$', views.CartListView.as_view(), name='cart_list'),
    url(r'^cart/create/$', views.CartCreateView.as_view(), name='cart_create'),
    url(r'^orders/$', views.PendingOrders.as_view(), name='pending_orders'),
    ]
