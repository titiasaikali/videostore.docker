# movies/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    q = request.GET.get("q", "")
    movies = Movie.objects.all()
    if q:
        movies = movies.filter(MovieTitle__icontains=q)
    return render(request, "movies/movie_list.html", {"movies": movies, "q": q})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, MovieID=pk)
    return render(request, "movies/movie_detail.html", {"movie": movie})

def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie created.")
            return redirect("movies:movie_list")
    else:
        form = MovieForm()
    return render(request, "movies/movie_form.html", {"form": form, "mode": "create"})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, MovieID=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie updated.")
            return redirect("movies:movie_detail", pk=movie.MovieID)
    else:
        form = MovieForm(instance=movie)
    return render(
        request, "movies/movie_form.html",
        {"form": form, "mode": "edit", "movie": movie}
    )

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, MovieID=pk)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Movie deleted.")
        return redirect("movies:movie_list")
    return render(request, "movies/movie_confirm_delete.html", {"movie": movie})
