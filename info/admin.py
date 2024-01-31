from django.contrib import admin
from .models import StudentsModel
# Register your models here.

@admin.register(StudentsModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','profile','name','enr','status','color','task']