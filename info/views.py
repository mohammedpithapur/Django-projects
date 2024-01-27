from django.shortcuts import render,redirect
from django.views import View
from .models import Students
from .form import Addstudents,Editstudents
# Create your views here.

class HOME(View):
    def get(self,request):
        stdi=Students.objects.all()
        return render(request, 'main/home.html' ,{'stu':stdi})
class Add(View):
    def get(self,request):
        addit= Addstudents()
        return render(request, 'main/add.html', {"add":addit})
    def post(self,request):
        addit = Addstudents(request.POST, request.FILES)
        print(addit)
        if addit.is_valid():
            addit.save()
            return redirect('/')
        else:
            return render(request, 'main/add.html', {"add":addit})
class Delete(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        studata=Students.objects.get(id=id)
        studata.delete()
        return redirect('/')
    
class Edit(View):
    def get(self,request, id):
        s=Students.objects.get(id=id)
        fm=Editstudents(instance=s)
        return render(request, 'main/edit.html',{'form':fm})
    def post(self, request, id):
        s=Students.objects.get(id=id)
        fm=Editstudents(request.POST,request.FILES, instance=s)
        if fm.is_valid():
            fm.save()
            return redirect('/')