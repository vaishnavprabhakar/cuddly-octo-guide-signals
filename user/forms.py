from typing import Any
from django import forms


class PollForm(forms.Form):
    name = forms.CharField(required=False,max_length=56,)
