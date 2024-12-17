from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog.models import Post

from .forms import ProductForm


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_active=True)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.context = super().get_object(queryset)
        self.context.counted_views += 1
        self.context.save()
        return self.context


class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    form_class = ProductForm


class PostUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
    form_class = ProductForm

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
