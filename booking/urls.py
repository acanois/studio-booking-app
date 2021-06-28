from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('get_all', views.UserListView.as_view(), name='get-all')
]