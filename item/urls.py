from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.List.as_view(), name='list'),
    path('search/', views.Search.as_view(), name='search'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
    path('show/', views.Show.as_view(), name='show'),
    path('show_search/', views.ShowSearch.as_view(), name='show_search'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail'),
]
