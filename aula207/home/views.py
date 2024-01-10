from django.shortcuts import render

# Create your views here.
def home(request):
    print("HOME")
    return render(request, 'home/index.html')

