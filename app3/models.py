from django.db import models

# Create your models here.


class Places(models.Model):
    place = models.CharField(max_length=80)

    def __str__(self):
        return self.place


class Types(models.Model):
    typ = models.CharField(max_length=20)

    def __str__(self):
        return self.typ


class Status(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status


# class Progress(models.Model):
#     stage = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.stage


class Vendors(models.Model):
    vendor = models.CharField(max_length=20)

    def __str__(self):
        return self.vendor


# class Goals(models.Model):
#     goal = models.CharField(max_length=80)
#
#     def __str__(self):
#         return self.goal


class Partners(models.Model):
    partner = models.CharField(max_length=30)

    def __str__(self):
        return self.partner


class People(models.Model):
    fio = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    partner = models.ForeignKey(Partners, on_delete=models.SET(1))
    comment = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.fio


class Shipments(models.Model):
    ship_id = models.CharField(max_length=15, default='Не определено')
    partner = models.ForeignKey(Partners, on_delete=models.SET(1))
    contact = models.ForeignKey(People, on_delete=models.SET(1))
    # foto = models.ImageField(upload_to='foto/%Y/%m/%d/')
    # docs = models.FileField(upload_to='docs/%Y/%m/%d/')
    in_date = models.DateField(auto_now=True)
    # in_actor = models.ForeignKey(People, on_delete=models.SET(1))
    out_date = models.DateField(blank=True)
    # out_actor = models.ForeignKey(People, on_delete=models.SET(1)
    ready = models.BooleanField(default=False)
    comment = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.ship_id


# class Tasks(models.Model):
#     src = models.CharField(max_length=80)
#     goal = models.ForeignKey(Goals, on_delete=models.SET(1))
#     stage = models.ForeignKey(Progress, on_delete=models.SET(1)
#     actor = models.ForeignKey(People, on_delete=models.SET(1)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     comment = models.TextField(max_length=255)
#
#     def __str__(self):
#         return self.goal


class Equipment(models.Model):
    name = models.CharField(max_length=20)
    vendor = models.ForeignKey(Vendors, on_delete=models.SET(1))
    typ = models.ForeignKey(Types, on_delete=models.SET(1))
    sn = models.CharField(max_length=20)
    shipment = models.ForeignKey(Shipments, blank=True, on_delete=models.SET(1))
    # task = models.ForeignKey(Tasks, on_delete=models.SET(1))
    responsible = models.ForeignKey(People, on_delete=models.SET(1))
    place = models.ForeignKey(Places, on_delete=models.SET(1))
    integrity = models.BooleanField(default=True)
    status = models.ForeignKey(Status, on_delete=models.SET(1))
    tech = models.TextField(max_length=4096, blank=True)
    comment = models.TextField(max_length=512, blank=True)

    def __str__(self):
        return self.name
