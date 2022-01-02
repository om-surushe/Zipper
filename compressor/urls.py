from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('compressor/', views.compressor, name='compressor'),
    path('decompressor/<str:id>', views.decompressor, name='decompressor'),
    path('ecodetext/', views.ecodetext, name='ecodetext'),
]
