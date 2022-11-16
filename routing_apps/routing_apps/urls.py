"""routing_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls','home'),namespace='home')),#here include(('home.urls','home'),namespace='home') homme .url is the name of the file urls inside home folder and namespace = "home" is also the name of the app folder name and this should be liek this for all 
    path('add_member/',include(('add_member.urls','add_member'),namespace='add_member')),
    path('search_student/',include(('search_student.urls','search_student'),namespace='search_student')),
    path('update_student/',include(('update_student.urls','update_student'),namespace ='update_student')),
    path('delete_student/',include(('delete_student.urls','delete_student'),namespace='delete_student')),
]
