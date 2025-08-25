from django.db import models

# Create your models here.
from django.db import models

# Student Model
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

