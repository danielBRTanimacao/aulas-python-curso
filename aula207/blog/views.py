from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')
    return render(request, 'blog/index.html')

def exemplo(request):
    print('blog')
    return render(request, 'blog/exemplo.html')