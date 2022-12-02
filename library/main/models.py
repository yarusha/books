from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField('Name', max_length=50)
    author = models.CharField('Author', max_length=50)
    text = models.TextField('About')
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    count = models.IntegerField('Quantity', default=1)
    createed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'