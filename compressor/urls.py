from django.urls import path

from . import views

urlpatterns = [
    path('compressor/', views.home, name='home'),
    path('decompressor/<str:id>', views.decompressor, name='decompressor'),
    path('ecodetext/', views.ecodetext, name='ecodetext'),
]
