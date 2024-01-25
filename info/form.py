from django import forms
from .models import Students

class Addstudents(forms.ModelForm):
    class Meta:
        model=Students
        fields=("name","enr","marks")
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'enr':forms.NumberInput(attrs={'class':'form-control'}),
            'marks':forms.NumberInput(attrs={'class':'form-control'})
        }