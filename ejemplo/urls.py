from django.urls import path
from ejemplo import views

urlpatterns = [path('', views.catalog, name='catalog')]