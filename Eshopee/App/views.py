from django.shortcuts import render
from App.models import Category
def Base(request):
    return render(request,'base.html')


def index(request):
    category=Category.objects.all()
    context={
        'category':category
        }
    return render(request,'index.html',context)

# Create your views here.

