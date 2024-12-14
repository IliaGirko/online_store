from django.urls import path

from blog.apps import BlogConfig

from . import views

app_name = BlogConfig.name

urlpatterns = [
    path("blogs/post_list/", views.PostListView.as_view(), name="post_list"),
    path("blogs/post_list/<int:pk>/detail/", views.PostDetailView.as_view(), name="post_detail"),
    path("blogs/post_list/create", views.PostCreateView.as_view(), name="post_create"),
    path("blogs/post_list/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("blogs/post_list/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]
