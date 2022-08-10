from django.views.generic.list import ListView
from .models import Vendors, Status, Types, Places, Partners, People, Shipments, Equipment


class ListEquipmentSmallView(ListView):
    model = Equipment
    template_name = 'List/list_equipment_small.html'
    ordering = 'name'
    fields = ['name', 'typ', 'sn', 'shipment', 'place', 'status']



class ListShipmentsView(ListView):
    model = Shipments
    template_name = 'List/list_shipments.html'
    ordering = 'in_date'
    fields = '__all__'



class ListPeopleView(ListView):
    model = People
    template_name = 'List/list_people.html'
    ordering = 'fio'
    fields = '__all__'


class ListPartnersView(ListView):
    model = Partners
    template_name = 'List/list_partners.html'
    ordering = 'partner'
    fields = '__all__'


class ListVendorView(ListView):
    model = Vendors
    template_name = 'List/list_vendors.html'
    ordering = 'vendor'
    fields = '__all__'



class ListPlacesView(ListView):
    model = Places
    template_name = 'List/list_places.html'
    ordering = 'place'
    fields = '__all__'


class ListStatusView(ListView):
    model = Status
    template_name = 'List/list_status.html'
    ordering = 'status'
    fields = '__all__'


class ListTypeView(ListView):
    model = Types
    template_name = 'List/list_types.html'
    ordering = 'typ'
    fields = '__all__'
