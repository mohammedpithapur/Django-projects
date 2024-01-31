from django import forms
from .models import StudentsModel

class Profedit(forms.ModelForm):
    class Meta:
        model=StudentsModel
        fields=('profile',"name","enr",'task',"status",'color')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'enr':forms.NumberInput(attrs={'class':'form-control'}),
            'task':forms.Textarea(),
            'status':forms.CheckboxInput(),
            'color':forms.TextInput(attrs={'class':'form-control'})
        }

