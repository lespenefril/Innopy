from django.views.generic.edit import DeleteView
from .models import Vendors, Status, Types, Places, Partners, People, Shipments, Equipment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class DelEquipmentView(LoginRequiredMixin, DeleteView):
    model = Equipment
    success_url = reverse_lazy("equipment")
    template_name = "del_form.html"
    login_url = reverse_lazy("staff_login")


class DelShipmentView(LoginRequiredMixin, DeleteView):
    model = Shipments
    success_url = reverse_lazy("shipments")
    template_name = "del_form.html"
    login_url = reverse_lazy("staff_login")


class DelPeopleView(LoginRequiredMixin, DeleteView):
    model = People
    success_url = reverse_lazy("people")
    template_name = "del_form.html"
    login_url = reverse_lazy("staff_login")


class DelPartnerView(LoginRequiredMixin, DeleteView):
    model = Partners
    success_url = reverse_lazy("partners")
    template_name = "del_form.html"
    login_url = reverse_lazy("staff_login")


class DelPlaceView(LoginRequiredMixin, DeleteView):
    model = Places
    success_url = reverse_lazy("places")
    template_name = "del_form.html"
    login_url = reverse_lazy("staff_login")


class DelVendorView(LoginRequiredMixin, DeleteView):
    model = Vendors
    success_url = reverse_lazy("vendors")
    template_name = "del_form.html"
    login_url = reverse_lazy("staff_login")


class DelStatusView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy("status")
    template_name = "del_form.html"
    login_url = reverse_lazy("staff_login")


class DelTypeView(LoginRequiredMixin, DeleteView):
    model = Types
    success_url = reverse_lazy("types")
    template_name = "del_form.html"
    login_url = reverse_lazy("staff_login")
