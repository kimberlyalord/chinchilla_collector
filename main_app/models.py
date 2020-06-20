from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Chinchilla(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'chinchilla_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    chinchilla = models.ForeignKey(Chinchilla, on_delete=models.CASCADE)
    
    def __str__(self):
        return  f'{self.get_meal_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']
          
class Bath(models.Model):
    date = models.DateField('Bath Date')
    chinchilla = models.ForeignKey(Chinchilla, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_bath_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']
        
class Photo(models.Model):
    url = models.CharField(max_length=300)
    chinchilla = models.ForeignKey(Chinchilla, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Photo for chinchilla_id: {self.chinchilla_id} @{self.url}"