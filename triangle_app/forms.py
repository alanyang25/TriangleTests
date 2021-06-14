from django import forms
from .models import Length

class LengthModelForm(forms.ModelForm):
    class Meta:
        model = Length
        fields = '__all__'
        widgets = {
            'a': forms.NumberInput(attrs={'class': 'form-control', 'onkeyup': "myFunction()"}),
            'b': forms.NumberInput(attrs={'class': 'form-control', 'onkeyup': "myFunction()"}),
            'c': forms.NumberInput(attrs={'class': 'form-control', 'onkeyup': "myFunction()"}),
        }
        labels = {
            'a': 'Side A',
            'b': 'Side B',
            'c': 'Side C',
        }