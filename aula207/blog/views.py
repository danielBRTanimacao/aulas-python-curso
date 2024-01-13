from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')

    context = {
        'text': 'Ola agora sou o blog',
        'title': 'Blog - '
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):
    print('blog')

    context = {
        'text': 'Ola agora sou o exemplo blog',
        'title': 'Exemplo - '
    }

    return render(request, 'blog/exemplo.html', context)