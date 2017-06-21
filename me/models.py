from django.db import models


CHOICES=(("ADMIN", "admin"),("REGULAR", "Reg"))

class Snippet(models.Model):
   
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    role = models.CharField(choices=CHOICES, default='REGULAR', max_length=100)

    
