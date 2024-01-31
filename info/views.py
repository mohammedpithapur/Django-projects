from django.shortcuts import render,redirect
from django.views import View
from .models import StudentsModel
from .form import Addstudents,Editstudents
from .form import Editstudents,Profedit
# Create your views here.

class HOME(View):
    def get(self,request):
        stdi=StudentsModel.objects.all()
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
            return redirect('profadmin')
        else:
            return render(request, 'main/add.html', {"add":addit})
class Delete(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        studata=StudentsModel.objects.get(id=id)
        studata.delete()
        return redirect('profadmin')
    
class Edit(View):
    def get(self,request, id):
        s=StudentsModel.objects.get(id=id)
        fm=Editstudents(instance=s)
        return render(request, 'main/edit.html',{'form':fm})
    def post(self, request, id):
        s=StudentsModel.objects.get(id=id)
        fm=Editstudents(request.POST,request.FILES, instance=s)
        if fm.is_valid():
            fm.save()
            return redirect('/')
def profadmin(request):
    stdi=StudentsModel.objects.all()
    return render(request,'main/profadmin.html',{'stu':stdi})
class profEdit(View):
    def get(self,request, id):
        s=StudentsModel.objects.get(id=id)
        fm=Profedit(instance=s)
        return render(request, 'main/profedit.html',{'form':fm})
    def post(self, request, id):
        s=StudentsModel.objects.get(id=id)
        fm=Profedit(request.POST,request.FILES, instance=s)
        if fm.is_valid():
            fm.save()
            return redirect('profadmin')