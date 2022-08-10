from django.views.generic.edit import CreateView
from .models import Vendors, Status, Types, Places, Partners, People, Shipments, Equipment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class AddEquipmentView(LoginRequiredMixin, CreateView):
    model = Equipment
    template_name = 'add_form.html'
    success_url = reverse_lazy("equipment")
    fields = '__all__'
    login_url = reverse_lazy("staff_login")


class AddShipmentView(LoginRequiredMixin, CreateView):
    model = Shipments
    template_name = 'add_form.html'
    success_url = reverse_lazy("shipments")
    fields = '__all__'
    login_url = reverse_lazy("staff_login")


class AddPeopleView(LoginRequiredMixin, CreateView):
    model = People
    template_name = 'add_form.html'
    success_url = reverse_lazy("people")
    fields = '__all__'
    login_url = reverse_lazy("staff_login")


class AddPlacesView(LoginRequiredMixin, CreateView):
    model = Places
    template_name = 'add_form.html'
    success_url = reverse_lazy("places")
    fields = '__all__'
    login_url = reverse_lazy("staff_login")


class AddPartnerView(LoginRequiredMixin, CreateView):
    model = Partners
    template_name = 'add_form.html'
    success_url = reverse_lazy("partners")
    fields = '__all__'
    login_url = reverse_lazy("staff_login")


class AddVendorView(LoginRequiredMixin, CreateView):
    model = Vendors
    template_name = 'add_form.html'
    success_url = reverse_lazy("vendors")
    fields = '__all__'
    login_url = reverse_lazy("staff_login")


class AddStatusView(LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'add_form.html'
    success_url = reverse_lazy("status")
    fields = '__all__'
    login_url = reverse_lazy("staff_login")


class AddTypeView(LoginRequiredMixin, CreateView):
    model = Types
    template_name = 'add_form.html'
    success_url = reverse_lazy("types")
    login_url = reverse_lazy("staff_login")
    fields = "__all__"
