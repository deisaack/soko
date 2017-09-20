from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
]
