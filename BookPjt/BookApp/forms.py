from django import forms
from .models import Book_List
class BookForms(forms.ModelForm):
    class Meta:
        model=Book_List
        fields=['name','desc','year','img']