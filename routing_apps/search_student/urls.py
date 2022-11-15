from django.urls import path
from. import views

urlpatterns = [
    path('search',views.search,name='search'),
    path('to_add',views.to_add,name='to_add'),
    path('to_update',views.to_update,name='to_update'),
    path('to_delete',views.to_delete,name='to_delete'),
    path('to_home',views.to_home,name='to_home'),
]