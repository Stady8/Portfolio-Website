from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def webApp(request):
    return render(request,'webApp.html')

def mazegame(request):
    return render(request,'maze.html')

def vrgame(request):
    return render(request,'vrgame.html')

def trailer(request):
    return render(request,'trailer.html')

def resume(request):
    return render(request,'resume.html')

    
