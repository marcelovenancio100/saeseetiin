from django.urls import path

from . import views

app_name = 'situation'

urlpatterns = [
    path('', views.List.as_view(), name='list'),
    path('search/', views.Search.as_view(), name='search'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
]
