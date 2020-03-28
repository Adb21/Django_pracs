from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    isbn = models.CharField(max_length=100)
    authors = models.CharField(max_length=200)
    original_publication_year = models.IntegerField()
    original_title = models.CharField(max_length=200)
    language_code = models.CharField(max_length=200)
    average_rating = models.FloatField()
    image_url = models.CharField(max_length=500, default="https://ibf.org/site_assets/img/placeholder-book-cover-default.png")

    def __str__(self):
        return self.book_id

   