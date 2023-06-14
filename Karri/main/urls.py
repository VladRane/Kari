from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('kontaktu', views.kontaktu, name='kontaktu'),
    path('onas', views.onas, name='onas'),
]

