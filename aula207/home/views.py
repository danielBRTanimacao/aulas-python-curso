from django.shortcuts import render

# Create your views here.
def home(request):
    print("HOME")

    context = {
        'text': 'Estamos na Home',
        'title': 'Index - ',
    }

    return render(request, 'home/index.html', context)

