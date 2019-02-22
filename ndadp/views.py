from django.shortcuts import render

# Create your views here.

def root(request):
    context = {
        'shi': 'Django app'
    }
    return render(request,'ndadp/root.html',context)