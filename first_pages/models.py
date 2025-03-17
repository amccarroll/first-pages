from django.db import models

# Create your models here.

class BookPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    page_number = models.IntegerField()
    book_title = models.CharField(max_length=200)
    purchase_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.book_title} - Page {self.page_number}"
