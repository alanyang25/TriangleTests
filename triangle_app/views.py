from django.shortcuts import render
from .forms import LengthModelForm

def index(request):
    
    form = LengthModelForm()

    return render(request, "triangle_app/index.html", {
        'form': form
    })