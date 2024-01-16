from django.shortcuts import render
from blog.data import posts


def blog(request):
    print('blog')

    context = {
        'text': 'Ola agora sou o blog',
        'title': 'Blog - ',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):
    print('blog')

    context = {
        'text': 'Ola agora sou o exemplo blog',
        'title': 'Exemplo - '
    }

    return render(request, 'blog/exemplo.html', context)