from django.views.generic.edit import UpdateView
from .models import Vendors, Status, Types, Places, Partners, People, Shipments, Equipment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdEquipmentView(LoginRequiredMixin, UpdateView):
    model = Equipment
    fields = '__all__'
    template_name = 'upd_form.html'
    success_url = reverse_lazy("equipment")
    login_url = reverse_lazy("staff_login")


class UpdShipmentView(LoginRequiredMixin, UpdateView):
    model = Shipments
    fields = '__all__'
    template_name = 'upd_form.html'
    success_url = reverse_lazy("shipments")
    login_url = reverse_lazy("staff_login")


class UpdPeopleView(LoginRequiredMixin, UpdateView):
    model = People
    fields = '__all__'
    template_name = 'upd_form.html'
    success_url = reverse_lazy("people")
    login_url = reverse_lazy("staff_login")


class UpdVendorView(LoginRequiredMixin, UpdateView):
    model = Vendors
    fields = ['vendor']
    template_name = 'upd_form.html'
    success_url = reverse_lazy("vendors")
    login_url = reverse_lazy("staff_login")


class UpdPartnersView(LoginRequiredMixin, UpdateView):
    model = Partners
    fields = ['partner']
    template_name = 'upd_form.html'
    success_url = reverse_lazy("partners")
    login_url = reverse_lazy("staff_login")


class UpdPlacesView(LoginRequiredMixin, UpdateView):
    model = Places
    fields = ['place']
    template_name = 'upd_form.html'
    success_url = reverse_lazy("places")
    login_url = reverse_lazy("staff_login")


class UpdStatusView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['status']
    template_name = 'upd_form.html'
    success_url = reverse_lazy("status")
    login_url = reverse_lazy("staff_login")


class UpdTypeView(LoginRequiredMixin, UpdateView):
    model = Types
    fields = ['typ']
    template_name = 'upd_form.html'
    success_url = reverse_lazy("types")
    login_url = reverse_lazy("staff_login")
