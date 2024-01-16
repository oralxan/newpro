from django.views.generic import(
    ListView,
    DetailView
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
)

from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class BookList(ListView):
    model = Book
    template_name = 'book/books.html'
    context_object_name = 'books'
class BookDetail(DetailView):
    model = Book
    template_name = 'book/books_detail.html'
    context_object_name = 'books'
