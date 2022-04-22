from django.db import models

# from django.contrib.auth import get_user_model

# User = get_user_model()


class Ticker(models.Model):
    ticker = models.CharField(max_length=200)
    current_price = models.URLField(max_length=200)
