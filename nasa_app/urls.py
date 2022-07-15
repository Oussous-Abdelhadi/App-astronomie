from django import views
from django.contrib import admin
from django.urls import path
import space.views as views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='home'),
    path('api-nasa/', views.apiNasa, name='api-nasa'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()