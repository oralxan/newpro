from django.views.generic import (
    ListView,
    DetailView
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book

class BookList(ListView):
    model = Book
    template_name = 'book/books.html'
    context_object_name = 'books'

class BookDetail(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book/book_create.html'
    context_object_name = 'book_create'
    fields = (
        'name',
        'description',
        'price',
        'cover'
    )
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BookUpdate(UpdateView):
    model = Book
    template_name = 'book/book_update.html'
    context_object_name = 'book_update'
    fields = (
        'name',
        'description',
        'price',
        'cover'
    )
    success_url = reverse_lazy('book_list')
class BookDelete(DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('book_list')
    context_object_name = 'book_delete'
    