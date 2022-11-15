from django.urls import path
from. import views

urlpatterns = [
    path('delete',views.delete,name='delete'),
    path('delete_record',views.delete_record, name ='delete_record'),
    path('to_update',views.to_update, name = 'to_update'),
    path('to_search',views.to_search, name = 'to_search'),
    path('to_add',views.to_add, name = 'to_add'),
    path('to_home',views.to_home, name = 'to_hom'),
]