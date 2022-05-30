from django.db import models

# Create your models here.


class dogs (models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    type = models.TextField(max_length=500)
    AKC = models.BooleanField(default=False)
    CKC = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']