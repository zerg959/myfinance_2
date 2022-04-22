from django import forms
from .models import Ticker


class TickerCheckForm(forms.Form):
    ticker = forms.CharField(max_length=255)
