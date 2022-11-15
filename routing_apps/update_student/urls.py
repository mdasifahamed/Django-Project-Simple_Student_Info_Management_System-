from django.urls import path
from. import views

urlpatterns = [
    path('update',views.update,name='update'),
    path('update_record',views.update_record, name = 'update_record'),
    path('to_home',views.to_home, name ='to_home'),
    path('to_add', views.to_add , name = 'to_add'),
    path('to_search',views.to_search, name= 'to_search'),
    path('to_delete', views.to_delete, name = 'to_search')
]