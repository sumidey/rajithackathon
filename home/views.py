from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def homePg(request):
    return render(request,'home.html')