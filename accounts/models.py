from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    user_img = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20)
    about = models.TextField(blank=True)
    def __str__(self):
        return self.email


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    from_date = models.DateField()
    till_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    def __str__(self):
        return self.company


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    from_date = models.DateField()
    till_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=True)
    description = models.TextField()
    def __str__(self):
        return self.school


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    scale = models.SmallIntegerField()
    is_language = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
