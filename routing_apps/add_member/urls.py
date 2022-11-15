from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('to_home', views.to_home, name='to_home'),
    path('to_update', views.to_update, name='to_update'),
    path('to_delete', views.to_delete, name='to_delete'),
    path('to_search', views.to_search, name='to_search'),
]
