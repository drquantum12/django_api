from django.db import models
from django.contrib.auth.models import User  # importing user from default user object given in django admin
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_rating(self):   # to get the number of ratings of that particular movie
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)
    def avg_rating(self):    # to get average rating
        sum=0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0




class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),
    MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','movie'),)  # so that a user cant rate same movie twice
        index_together = (('user','movie'),)

    # min-max validators are for validating input values


