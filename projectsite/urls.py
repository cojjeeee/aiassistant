from django.contrib import admin
from django.urls import path, include
from aiapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', home, name='home'),
]