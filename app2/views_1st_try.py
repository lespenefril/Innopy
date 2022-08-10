from django.shortcuts import HttpResponse, render
from django.views import generic
from django.views.generic.edit import FormView
from .models import Recruits, Faculty, Speciality
from .forms import FacultyForm


# Create your views here.
def wrong():
    # функция служебная, не монтируется на эндпойнт
    return '<a href="choice"> Request Page </a>'

def hellow(request):
    return HttpResponse('Hello World!!')

def ret_recr_all(request):
    # процедурная вьюшка
    reqall = Recruits.objects.all()
    resp1 = []
    for row in reqall:
        resp1.append(row.book_id + ' | ' + row.pad_nm + ' | ' + str(row.fac_num)\
        + ' | ' + str(row.spec_code) + ' | ' + str(row.lvl) + '<BR>')
    resp1.append(wrong())
    return HttpResponse(resp1)


def start(request):
    # вьюшка рендерит стартовую страницу
    return render(request, 'start.html')


def choice(request):
    # вьюшка рендерит общую страницу с формами запросов CRUD
    return render(request, 'choice.html')


def c_recr(request):
    # процедурная вьюшка CREATE
    # в settings.py отключен 'django.middleware.csrf.CsrfViewMiddleware'
    if request.method == "GET":
        return HttpResponse(wrong())
    else:
        Recruits(
            book_id=request.POST["book"],
            pad_nm=request.POST["name"],
            fac_num_id=int(request.POST["fac"]),
            spec_code_id=request.POST["spec"],
            lvl=int(request.POST["level"])
        ).save()
        return HttpResponse("OK<br>" + wrong())

def r_recr(request):
    # процедурная вьюшка Retrieve
    # в settings.py отключен 'django.middleware.csrf.CsrfViewMiddleware'
    if request.method == "GET":
        return HttpResponse(wrong())
    else:
        if request.POST["field"] == 'BookID':
            resp = Recruits.objects.filter(book_id=request.POST["reqval"])
        elif request.POST["field"] == 'name':
            resp = Recruits.objects.filter(pad_nm=request.POST["reqval"])
        elif request.POST["field"] == 'faculty':
            resp = Recruits.objects.filter(fac_num_id=request.POST["reqval"])
        elif request.POST["field"] == 'speciality':
            resp = Recruits.objects.filter(spec_code=request.POST["reqval"])
        elif request.POST["field"] == 'level':
            resp = Recruits.objects.filter(lvl=request.POST["reqval"])
        resp1 = []
        for row in resp:
            resp1.append(row.book_id + ' | ' + row.pad_nm + ' | ' + str(row.fac_num) \
                         + ' | ' + str(row.spec_code) + ' | ' + str(row.lvl) + '<BR>')
        resp1.append("<br>OK<br>" + wrong())
        return HttpResponse(resp1)

def u_recr(request):
    # процедурная вьюшка Update
    # в settings.py отключен 'django.middleware.csrf.CsrfViewMiddleware'
    if request.method == "GET":
        return HttpResponse(wrong())
    else:
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
        return HttpResponse("<br>OK<br>" + wrong())
def d_recr(request):
    # процедурная вьюшка Delete
    # в settings.py отключен 'django.middleware.csrf.CsrfViewMiddleware'
    if request.method == "GET":
        return HttpResponse(wrong())
    if request.method == "POST":
        book = request.POST["book"]
        Recruits.objects.get(book_id=book).delete()
        return HttpResponse("<br>OK<br>" + wrong())
    return HttpResponse(wrong())

class AddFaculty(FormView):
    def get(self, request):
        return render(request, "FacFormC.html")

    def post(self, request):
        FacultyForm(request.POST).save()
        return HttpResponse("OK")


