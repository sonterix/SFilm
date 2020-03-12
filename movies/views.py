from django.views.generic import ListView, DetailView
from .models import Movie


class MovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'movies/movie_details.html'

