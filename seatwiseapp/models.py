from django.db import models


# Create your models here.

class signupmodel(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.firstname



class cardmodel(models.Model):
    image=models.FileField(upload_to='seatwiseapp/static')
    cardname=models.CharField(max_length=20)
    genres=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    youtube=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    duration=models.CharField(max_length=10)
    about=models.CharField(max_length=500)
    def __str__(self):
        return self.cardname


class seatselection1(models.Model):
    movie = models.ForeignKey(cardmodel, on_delete=models.CASCADE)  # ForeignKey relationship to cardmodel
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=15)
    selectedseats = models.CharField(max_length=100)
    # ticket_cost = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    def __str__(self):
        return self.selectedseats
