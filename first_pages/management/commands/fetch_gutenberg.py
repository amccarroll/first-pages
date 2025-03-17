from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
import re
from bs4 import BeautifulSoup
from first_pages.models import BookPage
import time
import random

class Command(BaseCommand):
    help = 'Fetches books from Project Gutenberg and stores them in the database'

    def add_arguments(self, parser):
        parser.add_argument('--num-books', type=int, default=5, help='Number of books to fetch')
        parser.add_argument('--pages-per-book', type=int, default=5, help='Number of pages to store per book')

    def clean_text(self, text):
        # Remove headers and footers
        text = re.sub(r'Project Gutenberg.*?EBook.*?\n', '', text, flags=re.DOTALL)
        text = re.sub(r'End of Project Gutenberg.*?EBook.*?\n', '', text, flags=re.DOTALL)
        
        # Split into paragraphs
        paragraphs = text.split('\n\n')
        
        # Find the first substantial paragraph that's not metadata
        start_index = 0
        for i, para in enumerate(paragraphs):
            # Skip empty paragraphs
            if not para.strip():
                continue
                
            # Skip paragraphs that are just metadata
            if re.match(r'^(Chapter|Table of Contents|Introduction|Preface|Author\'s Note|Copyright|All rights reserved|Project Gutenberg|End of Project Gutenberg)', para.strip(), re.IGNORECASE):
                continue
                
            # Skip paragraphs that are too short (likely metadata)
            if len(para.strip()) < 50:
                continue
                
            # Skip paragraphs that are just numbers or roman numerals
            if re.match(r'^[\dIVX\.\s]+$', para.strip()):
                continue
                
            # If we find a substantial paragraph that's not metadata, start from there
            start_index = i
            break
        
        # Join paragraphs starting from the first substantial one
        text = '\n\n'.join(paragraphs[start_index:])
        
        # Clean up any remaining metadata
        text = re.sub(r'^\s*Chapter \d+.*?\n', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\s*[IVX]+\.\s*\n', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\s*[IVX]+\.\s*', '', text, flags=re.MULTILINE)
        
        # Remove multiple newlines
        text = re.sub(r'\n\s*\n', '\n\n', text)
        
        return text.strip()

    def split_into_pages(self, text, pages_per_book):
        # Take only the first portion of the book (roughly 1/10th)
        # This ensures we only get the beginning of the story
        text = text[:len(text) // 10]
        
        # Split text into roughly equal pages
        paragraphs = text.split('\n\n')
        pages = []
        current_page = []
        current_length = 0
        target_length = len(text) // pages_per_book

        for para in paragraphs:
            if current_length + len(para) > target_length and current_page:
                pages.append('\n\n'.join(current_page))
                current_page = []
                current_length = 0
            current_page.append(para)
            current_length += len(para)

        if current_page:
            pages.append('\n\n'.join(current_page))

        return pages[:pages_per_book]  # Ensure we only return exactly pages_per_book pages

    def handle(self, *args, **options):
        num_books = options['num_books']
        pages_per_book = options['pages_per_book']

        # List of popular Gutenberg books (you can expand this)
        gutenberg_books = [
            ('1342', 'Pride and Prejudice'),
            ('1661', 'The Adventures of Sherlock Holmes'),
            ('74', 'The Adventures of Tom Sawyer'),
            ('1952', 'The Yellow Wallpaper'),
            ('1080', 'A Modest Proposal'),
            ('11', 'Alice\'s Adventures in Wonderland'),
            ('2701', 'Moby Dick'),
            ('98', 'A Tale of Two Cities'),
            ('345', 'Dracula'),
            ('84', 'Frankenstein')
        ]

        # Randomly select books
        selected_books = random.sample(gutenberg_books, min(num_books, len(gutenberg_books)))

        for book_id, title in selected_books:
            self.stdout.write(f'Fetching {title}...')
            
            try:
                # Fetch book from Gutenberg
                url = f'https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt'
                response = requests.get(url)
                response.raise_for_status()
                
                # Clean and process the text
                text = self.clean_text(response.text)
                pages = self.split_into_pages(text, pages_per_book)
                
                # Store pages in database
                for i, page_content in enumerate(pages[:pages_per_book], 1):
                    BookPage.objects.create(
                        book_title=title,
                        title=f'Chapter 1: Page {i}',
                        content=page_content,
                        page_number=i,
                        purchase_link=f'https://www.gutenberg.org/ebooks/{book_id}'
                    )
                
                self.stdout.write(self.style.SUCCESS(f'Successfully added {title}'))
                
                # Be nice to Gutenberg's servers
                time.sleep(1)
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error fetching {title}: {str(e)}'))
                continue

        self.stdout.write(self.style.SUCCESS(f'Successfully processed {len(selected_books)} books')) 