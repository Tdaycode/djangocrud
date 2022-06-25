from msilib.schema import ListView
from pyexpat import model
from typing import List
from django.shortcuts import render

# Create your views here.
class PostListView(ListView):
  model = Post



class PostCreateView(CreateView):
  model = Post
  fields  ="__all__"
  success_url = reverse_lazy("blog:all")


class PostDetailView(DetailView):
  model = Post


class PostUpdateView(UpdateView):
  model = Post
  fields = "__all__"
  success_url = reverse_lazy("blog:all")