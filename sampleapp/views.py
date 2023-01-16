from django.shortcuts import render, HttpResponse

def testfon(request):
    return HttpResponse("<H1> Hello  I'm Namfon <H1>")


def fon(request):
    name="Nattaporn"
    surname="Boonmala"
    age=21
    salary=30000.00
    context = {'name':name, 'surname':surname, 'age':age, 'salary':salary}
    return render(request, 'fon.html',context)


# Create your views here.
