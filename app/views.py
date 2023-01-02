from django.shortcuts import render

# Create your views here.
def loopings(request):
    d={'name':'gowthami','age':[21,34]}
    return render(request,'loopings.html',d)