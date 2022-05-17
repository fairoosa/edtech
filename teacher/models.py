from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # qualification
    profile_pic = models.ImageField(upload_to="teacher", null=True, blank=True)
    contact_number=models.CharField(max_length=15)
# Create your models here.
