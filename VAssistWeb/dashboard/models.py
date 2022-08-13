from sys import prefix
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DashboardModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateField()
    active = models.BooleanField(default=True)
    
    def __init__(self, *args, **kwargs):
        super(DashboardModel, self).__init__(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.username}-{self.active}"
