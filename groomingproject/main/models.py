from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    
class Master(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
