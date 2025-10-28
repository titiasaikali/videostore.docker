from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

CURRENT_YEAR = datetime.date.today().year

class Movie(models.Model):
    GENRE_CHOICES = [
        ("COMEDY", "Comedy"),
        ("ROMANCE", "Romance"),
        ("ACTION", "Action"),
        ("DRAMA", "Drama"),
        ("SCIFI", "Sci-Fi"),
        ("HORROR", "Horror"),
        ("THRILLER", "Thriller"),
        ("ANIMATION", "Animation"),
        ("OTHER", "Other"),
    ]

    MovieID      = models.CharField(max_length=20, unique=True)
    MovieTitle   = models.CharField(max_length=200)
    Actor1Name   = models.CharField(max_length=120)
    Actor2Name   = models.CharField(max_length=120, blank=True)
    DirectorName = models.CharField(max_length=120)
    MovieGenre   = models.CharField(max_length=20, choices=GENRE_CHOICES)
    ReleaseYear  = models.IntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(CURRENT_YEAR + 2)]
    )

    class Meta:
        ordering = ["MovieTitle"]

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"