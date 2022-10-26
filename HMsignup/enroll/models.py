from django.db import models

# Create your Sign Up models here.
class Sign_up(models.Model):
    username = models.CharField(max_length=10)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    

  
