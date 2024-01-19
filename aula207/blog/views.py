from typing import Any

from django.shortcuts import render
from blog.data import posts
from django.http import HttpRequest, Http404


def blog(request):
    print('blog')

    context = {
        'text': 'Ola agora sou o blog',
        'title': 'Blog - ',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

def post(request: HttpRequest, idPosts: int):

    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == idPosts:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post não existe mermão')

    context = {
        'text': f'Aqui está o post número {idPosts}',
        'title': found_post['title'] + ' - ',
        'varpost': found_post
    }

    return render(request, 'blog/post.html', context)

def exemplo(request):
    print('blog')

    context = {
        'text': 'Ola agora sou o exemplo blog',
        'title': 'Exemplo - '
    }

    return render(request, 'blog/exemplo.html', context)