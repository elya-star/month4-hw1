from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите книгу')
    author = models.CharField(max_length=100, verbose_name='укажите автора книги')
    description = models.TextField(verbose_name='укажите описание книги')
    image = models.ImageField(upload_to='book/', verbose_name='загрузите обложку книги', blank=True)
    create_date_book = models.PositiveIntegerField(verbose_name='укажите год выпуска книги', blank=True)
    file_book = models.FileField(upload_to='book/files/', verbose_name='загрузите файл книги', blank=True)
    book_url = models.URLField(verbose_name='укажите ссылку на книгу', blank=True)
    contact_email = models.EmailField(verbose_name='укажите свой email', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликована')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
            verbose_name = 'книга'
            verbose_name_plural = 'книги'

