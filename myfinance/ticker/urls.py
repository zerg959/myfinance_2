from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ticker/<ticker_request>/', views.ticker_detail_render),
    path('ticker/', views.ticker_list)
]
