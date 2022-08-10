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
from .views import hellow, start, success, DelFaculty, AddFaculty, AllRecruitsView, \
    CreateRecruitView, ReadRecruitView, UpdRecruitView, DelRecruitView

urlpatterns = [
    # path('', hellow),
    # path('start', start, name="start"),
    # path('success', success, name="success"),
    path('show_all', AllRecruitsView.as_view(), name="show_all"),
    path('rec_c', CreateRecruitView.as_view(), name="rec_c"),
    path('rec_r', ReadRecruitView.as_view(), name="rec_r"),
    path('rec_u', UpdRecruitView.as_view(), name="rec_u"),
    path('rec_d', DelRecruitView.as_view(), name="rec_d"),
    path('addfac', AddFaculty.as_view(), name="addfac"),
    path('delfac', DelFaculty.as_view(), name="delfac")
]
