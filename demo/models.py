from django.db import models
# Create your models here.
class task(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    def __str__(self):
        return self.id
    