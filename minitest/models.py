from django.db import models
from pygments.lexers import get_all_lexers

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])


# Create your models here.
class Board(models.Model):
    class Meta:
        ordering = ['created']

    owner = models.ForeignKey('auth.User',
                              related_name='board',
                              on_delete=models.CASCADE,
                              default='')
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    created = models.DateTimeField(auto_now_add=True)
