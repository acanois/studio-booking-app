from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_user', views.new_user, name='create-new-user'),
    path('get_all', views.get_all, name='get-all')
]