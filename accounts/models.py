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
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Experience(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200, blank=True)
    from_date = models.DateField()
    till_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=200, blank=True)
    from_date = models.DateField()
    till_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)
    scale = models.SmallIntegerField()
    language = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    framework = models.BooleanField(default=False)
    soft_skill = models.BooleanField(default=False)
    learning = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.name
