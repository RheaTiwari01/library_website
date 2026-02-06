from django import forms
from .models import Book, Publisher, Author


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'title',
            'publish_date',
            'author',
            'publisher'
        ]

        widgets = {
            'publish_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'authors': forms.CheckboxSelectMultiple()
        }


class PublishForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = ['name', 'country', 'website']


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['fname', 'lname', 'email']
