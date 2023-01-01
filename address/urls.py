from django.urls import path

from . import views

app_name = 'address'

urlpatterns = [
    path('', views.List.as_view(), name='list'),
    path('search/', views.Search.as_view(), name='search'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
]
