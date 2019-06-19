from django.shortcuts import render, HttpResponse, redirect
from .models import Book
from .models import Author

def index(request):
    context = {
       "all_books" : Book.objects.all(),
    }
    return render(request, "books_authors_app/index.html", context)

def display_book_dets(request,book_id):
    to_exclude = [author.id for author in Book.objects.get(id=book_id).authors.all()]
    context = {
        "book" : Book.objects.get(id=book_id),
        "book_authors" : Book.objects.get(id=book_id).authors.all(),
        "all_authors" : Author.objects.exclude(id__in=to_exclude),
    }
    return render(request, "books_authors_app/book_view.html", context)

def display_author(request):
    context = {
        "all_authors" : Author.objects.all(),
    }
    return render(request, "books_authors_app/authors.html", context)

def display_author_dets(request, auth_id):
    to_exclude = [book.id for book in Author.objects.get(id=auth_id).books.all()]
    context = {
        "author" : Author.objects.get(id=auth_id),
        "author_books" : Author.objects.get(id=auth_id).books.all(),
        "all_books" : Book.objects.exclude(id__in=to_exclude),
    }
    return render(request, "books_authors_app/author_view.html", context)

def add_book(request):
    if request.method == "POST":
        book_name = request.POST["title"]
        book_desc = request.POST["desc"]
        Book.objects.create(title=book_name, desc=book_desc)
    return redirect("/")

def add_author(request):
    if request.method == "POST":
        author_fname = request.POST["fn"]
        author_lname = request.POST["ln"]
        author_notes = request.POST["notes"]
        Author.objects.create(first_name= author_fname , last_name= author_lname , notes= author_notes)
    return redirect("/authors")

def add_author_to_book(request):
    if request.method == "POST":
        book_id = request.POST["b_id"]
        author_id = request.POST["a_id"]
        Book.objects.get(id=book_id).authors.add(Author.objects.get(id=author_id))
    return redirect("/book_dets/"+book_id)

def add_book_to_author(request):
    if request.method == "POST":
        book_id = request.POST["b_id"]
        author_id = request.POST["a_id"]
        Author.objects.get(id=author_id).books.add(Book.objects.get(id=book_id))
    return redirect("/author_dets/"+author_id)    


