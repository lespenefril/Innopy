from django.db import models


# Create your models here.
class Faculty(models.Model):
    fac_num = models.AutoField(primary_key=True)
    fac_name = models.TextField(max_length=30)
    def __str__(self):
        return self.fac_name

class Speciality(models.Model):
    spec_code = models.CharField(primary_key=True, max_length=2)
    spec_name = models.CharField(max_length=30)
    def __str__(self):
        return self.spec_name


class Recruits(models.Model):
    book_id = models.CharField(primary_key=True, max_length=15)
    pad_nm = models.CharField(max_length=50)
    fac_num = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    spec_code = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    lvl = models.IntegerField()
    def __str__(self):
        return self.pad_nm

class Mass(models.Model):
    mass_date = models.DateField(primary_key=True)
    mass_name = models.CharField(max_length=30)
    priest = models.ManyToManyField(Recruits)
    def __str__(self):
        return self.mass_name


