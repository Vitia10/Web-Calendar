from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.index_column, name='index_column'),
    path('calendar/',views.calendar,name='calendar'),
    path('testing/',views.testing,name='testing')
]