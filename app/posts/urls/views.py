from django.urls import path

from .. import views

app_name = 'posts'
urlpatterns = [
    # /posts/
    # views.post_list(request)
    path('', views.post_list, name='post-list'),

    # /posts/5/like/
    # views.post_like(request, pk=5)
    path('<int:pk>/like/', views.post_like, name='post-like'),

    # /posts/create/
    path('create/', views.post_create, name='post-create'),

    # /posts/3/comments/create/
    # views.post_create(request, post_pk=3)
    path('<int:post_pk>/comments/create/', views.comment_create, name='comment-create'),

    path('<int:post_pk>/comments/', views.comment_list),
]
