from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Bookmark


class BookmarkListView(ListView):  # R
    model = Bookmark  # bookmark_list -> HTML(bookmark_list.html)


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']  # '__all__', class를 사용하면 fields에 있는게 bookmark_create에서 input이 됨
    template_name_suffix = '_create'  # 원래는 '_form' -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')
