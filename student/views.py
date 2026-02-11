
from django.shortcuts import render
from .models import Department, Placementcell, Search
from .forms import SearchForm

# Create your views here.
def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def department(request):
    dict_DEPT = {
        'dept': Department.objects.all(),
    }
    return render(request, 'department.html',dict_DEPT)

def placementcell(request):
        dict_place = {
            'placement': Placementcell.objects.all(),
        }
        return render(request, 'placementcell.html',dict_place)

def contact(request):
    return render(request, 'contact.html')

def search(request):
    form =SearchForm
    dict_form={
        'form':form
    }
    return render(request, 'search.html',dict_form)