from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book
# Create your views here.
def create_book(request):
    book = Book.objects.create(
        name ='python',
        pub_date = '2020-2-2',
        author = 'IDK',
        readcount = 25,
    )

    return HttpResponse("create")