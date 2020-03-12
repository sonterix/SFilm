from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Category', max_length=160)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ActorDirector(models.Model):
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors and Directors'
        verbose_name_plural = 'Actors and Directors'


class Genre(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField('Title', max_length=100)
    tagline = models.CharField('Tagline', max_length=100, default='')
    description = models.TextField('Description')
    poster = models.ImageField('Poster', upload_to='posters/')
    year = models.PositiveSmallIntegerField('Year', default=date.today().year)
    country = models.CharField('Country', max_length=30)
    director = models.ManyToManyField(ActorDirector, verbose_name='director', related_name='film_director')
    actor = models.ManyToManyField(ActorDirector, verbose_name='actor', related_name='film_actor')
    genre = models.ManyToManyField(Genre, verbose_name='Genre')
    world_premiere = models.DateField('World Premiere', default=date.today)
    budget = models.PositiveIntegerField('Budget', default=0, help_text='Type in Dollars')
    worldwide_fees = models.PositiveIntegerField('Worldwide Fees', default=0, help_text='Type in Dollars')
    category = models.ForeignKey(Category, verbose_name='category', null=True, on_delete=models.SET_NULL)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    def get_absolute_urt(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='film', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie Shot'
        verbose_name_plural = 'Movie Shots'


class RatingStars(models.Model):
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating Star'
        verbose_name_plural = 'Rating Stars'


class Rating(models.Model):
    ip = models.CharField('IP address', max_length=15)
    star = models.ForeignKey(RatingStars, verbose_name='star', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name='movie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Reviews(models.Model):
    email = models.EmailField
    name = models.CharField('Name', max_length=100)
    text = models.CharField('Message', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='parent', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='film', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

