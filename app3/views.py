from django.shortcuts import render, HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .del_views import *
from .list_views import *
from .add_views import *
from .upd_views import *


# Create your views here.
class StaffLoginView(LoginView):
    template_name = 'login_form.html'
    next_page = 'start'


class StaffLogoutView(LogoutView):
    # template_name = 'login_form.html'
    next_page = 'start'


class EquipmentFullView(DetailView):
    model = Equipment
    template_name = 'equipment_detail.html'
    fields = '__all__'


def hello():
    return HttpResponse('Hello World?????')


def success(request):
    return render(request, "success.html")


def start(request):
    # вьюшка рендерит стартовую страницу
    return render(request, 'start.html')


def tasks(request):
    return render(request, "uc.html")


def progress(request):
    return render(request, "uc.html")


def goals(request):
    return render(request, "uc.html")
