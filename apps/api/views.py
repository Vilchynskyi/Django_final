from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..core.models import Book, Category
from .serializers import BookSerializer, CategorySerializer


class BookAPIView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('title',)
    search_fields = ('title',)
    ordering_fields = ('id', 'title')

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
