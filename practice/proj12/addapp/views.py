from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def input(request):
    return render(request, 'input.html')
def add(request):
    try:
        a=request.GET["t1"]
        x=int(a)
        b=request.GET["t2"]
        y=int(b)
        z=x+y
        return HttpResponse("<html><body bgcolor=cyan<h1>sum is:"+str(z)+"</h1></body></html>")
    except(ValueError):
        return HttpResponse("invalid input")
