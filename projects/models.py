from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    private = models.BooleanField(default=True)
    git_repo = models.URLField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    main_img = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    img_1 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    img_2 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    img_3 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    img_4 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
