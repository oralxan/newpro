from django.db.models import *
from django.contrib.auth.models import User
class Book(Model):

    author= ForeignKey(
        User,
        verbose_name='Author',
        on_delete=CASCADE
    )
    name=CharField(
        'name of book',
        max_length=128
    )
    description = TextField(
        'description of the book',
        blank=True,
        null=True
    )
    price = PositiveBigIntegerField(
        'price of the book',
        default=0

    )
    cover = ImageField(
        'cover image of the book',
        upload_to= 'books-images/'
    )
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name ='book'
        verbose_name_plural = 'books'
