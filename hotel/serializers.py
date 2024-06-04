from django.contrib.auth.models import User
from django.forms import models
from rest_framework import serializers
from .models import Room, Booking

class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return f'Room {self.number} - {self.type}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - {self.room.number}'

