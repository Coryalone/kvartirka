from django.db import models


class Article(models.Model):
    content = models.CharField(max_length=150, blank=True, verbose_name='Контент')

    def __str__(self):
        return self.content


class Comments(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(blank=True, verbose_name='Комментарий')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text
