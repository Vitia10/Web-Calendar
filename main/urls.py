
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/calendar/',include('index.urls')),
    path('', include('index.urls')),
    path('/testing/',include('index.urls')),
    path('admin/', admin.site.urls),
]
