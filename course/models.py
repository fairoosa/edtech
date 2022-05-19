from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=20)
    no_of_weeks=models.IntegerField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    is_active=models.BooleanField(default=False)