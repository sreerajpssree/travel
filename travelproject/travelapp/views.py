from django.http import HttpResponse
from django.shortcuts import render

from . models import Place


# Create your views here.
def demo(request):
    # Incorrect: place.object
    # Correct: place.objects
    places = Place.objects.all()
    # Rest of the code...
    return render(request,"index.html",{'result':places})
#def add(request):
#    x = int(request.GET['num1'])
#    y = int(request.GET['num2'])
#    res = x+y
#    sub = x-y
#    mul = x*y
#    return render(request,"add.html",{'result': res, 'result1': sub, 'result2': mul})

def contact(request):
    return HttpResponse("hello welcome")
#def register(request):
#    return render(request,"register.html")