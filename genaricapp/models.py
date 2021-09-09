from django.db import models

# Create your models here.
class ProductDetailes(models.Model):
    BOOK_CHOICE = [
        ('book','white'),
        ('book','black')
    ]

    YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
    ]

    book_name = models.CharField(max_length=120)
    book_color = models.CharField(max_length=120,choices=BOOK_CHOICE)
    book_price = models.IntegerField()
    book_cost_finall = models.IntegerField()
    book_title = models.CharField(max_length=120)
    book_year = models.CharField(max_length=100, choices=YEAR_IN_SCHOOL_CHOICES)
    book_address = models.TextField()
    book_image = models.ImageField(upload_to = 'images')


    def __str__(self) -> str:
        return self.book_name

