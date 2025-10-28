from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "MovieID", "MovieTitle", "Actor1Name", "Actor2Name",
            "DirectorName", "MovieGenre", "ReleaseYear",
        ]
        widgets = {
            "MovieID": forms.TextInput(attrs={"class": "form-control"}),
            "MovieTitle": forms.TextInput(attrs={"class": "form-control"}),
            "Actor1Name": forms.TextInput(attrs={"class": "form-control"}),
            "Actor2Name": forms.TextInput(attrs={"class": "form-control"}),
            "DirectorName": forms.TextInput(attrs={"class": "form-control"}),
            "MovieGenre": forms.Select(attrs={"class": "form-select"}),
            "ReleaseYear": forms.NumberInput(attrs={"class": "form-control"}),
        }