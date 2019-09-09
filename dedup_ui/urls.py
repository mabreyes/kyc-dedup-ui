from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path('verify', views.view_ui),
    path('view_list', views.view_list)
]