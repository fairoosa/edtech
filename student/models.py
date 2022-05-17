from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # qualification
    profile_pic = models.ImageField(upload_to="student", null=True, blank=True)
    contact_number=models.CharField(max_length=15)
