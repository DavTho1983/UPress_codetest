from django.db import models

class Headline(models.Model):
    article_link = models.TextField()
    headline = models.TextField()
    is_sarcastic = models.BooleanField()
