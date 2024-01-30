from django import forms
from .models import Students

# class Addstudents(forms.ModelForm):
#     class Meta:
#         model=Students
#         fields=('profile',"name","enr",'color')
#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'enr':forms.NumberInput(attrs={'class':'form-control'}),
#             # 'status':forms.CheckboxInput(),
#             'color':forms.TextInput(attrs={'class':'form-control'})
#         }
class Editstudents(forms.ModelForm):
    class Meta:
        model=Students
        fields=('profile',"name","status",'color')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.CheckboxInput(),
            'color':forms.TextInput(attrs={'class':'form-control'})
        }
# class Admin(forms.ModelForm):
#     class Meta:
#         model=Students
#         fields=('profile',"name","enr","status",'color')
#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'enr':forms.NumberInput(attrs={'class':'form-control'}),
#             'task':forms.Textarea(),
#             'status':forms.CheckboxInput(),
#             'color':forms.TextInput(attrs={'class':'form-control'})
#         }