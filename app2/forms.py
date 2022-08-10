from django import forms
from .models import Faculty, Recruits

class FacultyForm(forms.ModelForm):
    # fac_num = forms.IntegerField(label='Faculty Number', max_length=3)
    # fac_name = forms.CharField(label='Faculty Name', max_length=30)
    class Meta:
        model = Faculty
        fields = "__all__"


class CreateRecruitForm(forms.ModelForm):
    class Meta:
        model = Recruits
        fields = "__all__"