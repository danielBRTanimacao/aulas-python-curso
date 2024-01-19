from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:idPosts>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
