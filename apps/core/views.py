from .models import Book, Category
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    FormView,
)


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['category_list'] = Category.objects.all()
        return context


class CategoryView(DetailView):
    template_name = 'core/category.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['category']
        context['book_list'] = category.book_set.all()
        return context


class CategoryListView(ListView):
    template_name = 'core/category_list.html'
    queryset = Category.objects.all()


class BookDetailView(DetailView):
    template_name = 'core/book.html'
    model = Book


class BookListView(ListView):
    template_name = 'core/book_list.html'
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_qs = Book.objects.all()
        paginator = Paginator(book_qs, 1)
        page = self.request.GET.get('page')
        try:
            book_list = paginator.page(page)
        except PageNotAnInteger:
            book_list = paginator.page(1)
        except EmptyPage:
            book_list = paginator.page(paginator.num_pages)

        context['book_list'] = book_list
        return context
