from django.contrib import admin
from .models import Movie, RatingStars, Category, Genre, ActorDirector, MovieShots, Rating, Reviews


admin.site.register(Movie)
admin.site.register(RatingStars)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(ActorDirector)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(Reviews)
