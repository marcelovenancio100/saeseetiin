from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
