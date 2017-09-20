from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
CONTRAL= admin.site.urls
from shop.accounts import urls as acc_urls
from shop.products import urls as prod_urls
from shop.profiles import urls as proff_urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^prod/', include(prod_urls, namespace='products')),
    url(r'^proff/', include(proff_urls, namespace='profiles')),
    url(r'^contrler-room/', include(CONTRAL)),
    url(r'^', include(acc_urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
