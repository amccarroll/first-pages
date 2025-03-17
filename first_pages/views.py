from django.shortcuts import render
from django.views.generic import TemplateView
from .models import BookPage
from django.db.models import Min
import random

# Create your views here.

class HomeView(TemplateView):
    template_name = 'first_pages/home.html'

def random_first_page(request):
    # Get all unique book titles
    book_titles = BookPage.objects.values_list('book_title', flat=True).distinct()
    if not book_titles:
        return render(request, 'first_pages/random_first_page.html', {'error': 'No books available'})
    
    # Select a random book
    random_book = random.choice(book_titles)
    # Get the first page of the selected book
    first_page = BookPage.objects.filter(book_title=random_book).order_by('page_number').first()
    
    return render(request, 'first_pages/random_first_page.html', {
        'page': first_page,
        'book_title': random_book
    })

def additional_pages(request, book_title, current_page):
    # Get all pages after the current page for this book
    all_next_pages = BookPage.objects.filter(
        book_title=book_title,
        page_number__gt=current_page
    ).order_by('page_number')
    
    # Get the last page before slicing
    last_page = all_next_pages.last()
    
    # Get the next 5 pages
    next_pages = all_next_pages[:5]
    
    return render(request, 'first_pages/additional_pages.html', {
        'pages': next_pages,
        'book_title': book_title,
        'last_page': last_page
    })
