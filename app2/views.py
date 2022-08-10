from django.shortcuts import HttpResponse, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, View, DeleteView
from .models import Recruits, Faculty, Speciality
from .forms import FacultyForm


# Create your views here.

def hellow(request):
    return HttpResponse('Hello World!!')


def success(request):
    return render(request, "success.html")


def start(request):
    # вьюшка рендерит стартовую страницу
    return render(request, 'start.html')


class AllRecruitsView(generic.ListView):
    def get(self, request):
        return render(request, "rec_list.html", {"recruits": Recruits.objects.all()})


class CreateRecruitView(generic.ListView):
    def get(self, request):
        return render(request, "rec_c.html", {"specs": Speciality.objects.all()})


    def post(self, request):
        # CreateRecruitForm(request.POST).save()
        #Возможно, не работает из-за integer полей. Проверить позже.
        Recruits(
            book_id=request.POST["book"],
            pad_nm=request.POST["name"],
            fac_num_id=int(request.POST["fac"]),
            spec_code_id=request.POST["spec"],
            lvl=int(request.POST["level"])
        ).save()
        return render(request, "success.html")


class ReadRecruitView(generic.ListView):
    def get(self, request):
        return render(request, "rec_r.html")
    def post(self, request):
        if request.POST["field" ] == 'BookID':
            return render(request, "rec_list.html", {"recruits": Recruits.objects.filter(book_id=request.POST["reqval"])})
        elif request.POST["field" ] == 'name':
            return render(request, "rec_list.html", {"recruits": Recruits.objects.filter(pad_nm=request.POST["reqval"])})
        elif request.POST["field"] == 'faculty':
            return render(request, "rec_list.html", {"recruits": Recruits.objects.filter(fac_num_id=request.POST["reqval"])})
        elif request.POST["field" ] == 'speciality':
            return render(request, "rec_list.html", {"recruits": Recruits.objects.filter(spec_code=request.POST["reqval"])})
        elif request.POST["field"] == 'level':
            return render(request, "rec_list.html", {"recruits": Recruits.objects.filter(lvl=request.POST["reqval"])})
        else:
            raise Exception("Field incorrect")


class UpdRecruitView(View):
    def get(self, request):
        return render(request, "rec_u.html")
    def post(self, request):
        newval = request.POST["newval"]
        book = request.POST["book"]
        if request.POST["field"] == 'name':
            Recruits.objects.filter(book_id=book).update(pad_nm=newval)
        elif request.POST["field"] == 'faculty':
            Recruits.objects.filter(book_id=book).update(fac_num=newval)
        elif request.POST["field"] == 'speciality':
            Recruits.objects.filter(book_id=book).update(spec_code=newval)
        elif request.POST["field"] == 'level':
            Recruits.objects.filter(book_id=book).update(lvl=newval)
        return render(request, "success.html")


class DelRecruitView(View):
    def get(self, request):
        return render(request, "rec_d.html")
    def post(self, request):
        book = request.POST["book"]
        Recruits.objects.get(book_id=book).delete()
        return render(request, "success.html")


class AddFaculty(FormView):
    def get(self, request):
        return render(request, "FacFormC.html")

    def post(self, request):
        FacultyForm(request.POST).save()
        return render(request, "success.html")


class DelFaculty(DeleteView):
    model = Faculty
    fields = "__all__"
    template_name = "FacFormD.html"
    success_url = reverse_lazy("success")

    def get_object(self):
        pk = self.request.POST['fac_num']
        return self.get_queryset().filter(pk=pk).get()


    def get(self, request):
        return render(request, "FacFormD.html")
