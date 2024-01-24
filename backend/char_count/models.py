from django.db import models

class CharCount(models.Model):
    char_count = models.CharField(max_length=40)