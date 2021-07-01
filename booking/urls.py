from django.urls import path

from . import views

"""TODO:
    Switch these to re_path as needed
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('get-all', views.UserListView.as_view(), name='get_all'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='get_user_by_pk'),
    path('vue-app', views.vue_view, name='vue_app'),
]