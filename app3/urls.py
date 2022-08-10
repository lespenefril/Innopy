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
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from .viewsets import PeopleViewSet
from .views import hello, start, success, tasks, goals, progress, \
    AddVendorView, DelVendorView, UpdVendorView, ListVendorView, \
    ListStatusView, AddStatusView, UpdStatusView, DelStatusView, \
    ListTypeView, AddTypeView, UpdTypeView, DelTypeView, \
    ListPlacesView, AddPlacesView, UpdPlacesView, DelPlaceView, \
    ListPartnersView, AddPartnerView, UpdPartnersView, DelPartnerView, \
    ListPeopleView, AddPeopleView, UpdPeopleView, DelPeopleView, \
    ListShipmentsView, AddShipmentView, UpdShipmentView, DelShipmentView, \
    ListEquipmentSmallView, AddEquipmentView, UpdEquipmentView, DelEquipmentView, \
    EquipmentFullView, StaffLoginView, StaffLogoutView


router = routers.DefaultRouter()
router.register(r'people_api', PeopleViewSet, basename='people_api')

urlpatterns = [
    path('', hello),
    path('app3/start/', start, name="start"),
    path('app3/success/', success, name="success"),
    path('app3/equipment/', ListEquipmentSmallView.as_view(), name="equipment"),
    path('app3/equipment/add', AddEquipmentView.as_view(), name="equipment_add"),
    path('app3/equipment/upd/<int:pk>', UpdEquipmentView.as_view(), name="equipment_upd"),
    path('app3/equipment/del/<int:pk>', DelEquipmentView.as_view(), name="equipment_del"),
    path('app3/equipment/det/<int:pk>', EquipmentFullView.as_view(), name="equipment_det"),
    path('app3/shipments/', ListShipmentsView.as_view(), name="shipments"),
    path('app3/shipments/add', AddShipmentView.as_view(), name="shipment_add"),
    path('app3/shipments/upd/<int:pk>', UpdShipmentView.as_view(), name="shipment_upd"),
    path('app3/shipments/del/<int:pk>', DelShipmentView.as_view(), name="shipment_del"),
    path('app3/tasks/', tasks, name="tasks"),
    path('app3/people/', ListPeopleView.as_view(), name="people"),
    path('app3/people/add', AddPeopleView.as_view(), name="people_add"),
    path('app3/people/del/<int:pk>', DelPeopleView.as_view(), name="people_del"),
    path('app3/people/upd/<int:pk>', UpdPeopleView.as_view(), name="people_upd"),
    path('app3/partners/', ListPartnersView.as_view(), name="partners"),
    path('app3/partners/add', AddPartnerView.as_view(), name="partners_add"),
    path('app3/partners/del/<int:pk>', DelPartnerView.as_view(), name="partners_del"),
    path('app3/partners/upd/<int:pk>', UpdPartnersView.as_view(), name="partners_upd"),
    path('app3/places/', ListPlacesView.as_view(), name="places"),
    path('app3/places/add', AddPlacesView.as_view(), name="place_add"),
    path('app3/places/del/<int:pk>', DelPlaceView.as_view(), name="place_del"),
    path('app3/places/upd/<int:pk>', UpdPlacesView.as_view(), name="place_upd"),
    path('app3/types/', ListTypeView.as_view(), name="types"),
    path('app3/types/add', AddTypeView.as_view(), name="types_add"),
    path('app3/types/del/<int:pk>', DelTypeView.as_view(), name="types_del"),
    path('app3/types/upd/<int:pk>', UpdTypeView.as_view(), name="types_upd"),
    path('app3/status/', ListStatusView.as_view(), name="status"),
    path('app3/status/add', AddStatusView.as_view(), name="status_add"),
    path('app3/status/del/<int:pk>', DelStatusView.as_view(), name="status_del"),
    path('app3/status/upd/<int:pk>', UpdStatusView.as_view(), name="status_upd"),
    path('app3/vendors/', ListVendorView.as_view(), name="vendors"),
    path('app3/vendors/add', AddVendorView.as_view(), name="vendors_add"),
    path('app3/vendors/del/<int:pk>', DelVendorView.as_view(), name="vendors_del"),
    path('app3/vendors/upd/<int:pk>', UpdVendorView.as_view(), name="vendors_upd"),
    path('app3/progress/', progress, name="progress"),
    path('app3/goals/', goals, name="goals"),
    path('app3/login/', StaffLoginView.as_view(), name='staff_login'),
    path('app3/logout/', StaffLogoutView.as_view(), name='staff_logout'),
    path('app3/', include(router.urls))
]
