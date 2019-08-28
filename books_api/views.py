from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer


# Create a read-only endpoint for all book instances
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
