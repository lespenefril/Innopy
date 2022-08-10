"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import hellow, ret_recr_all, start, choice, c_recr, r_recr, u_recr, d_recr, AddFaculty

urlpatterns = [
    path('', hellow),
    path('start', start),
    path('choice', choice),
    path('show_all', ret_recr_all),
    path('create_r', c_recr),
    path('read_r', r_recr),
    path('update_r', u_recr),
    path('delete_r', d_recr),
    path('addfac', AddFaculty.as_view())
]