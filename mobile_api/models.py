from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

# Create your models here.
class MobileModel(models.Model):
    name=models.CharField(max_length=64)
    desc=models.TextField()
    company=models.ForeignKey(get_user_model(), on_delete=CASCADE)
    date_creation=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
