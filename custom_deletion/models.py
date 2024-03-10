from django.db import models

# Create your models here.
class Device(models.Model):
    STATUS_CHOICES=[
        ('ACTIVE','ACTIVE'),
        ('INACTIVE','INACTIVE')
    ]
    device_type=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    status=models.CharField(choices=STATUS_CHOICES,max_length=100)

    def __str__(self):
        return f'{self.device_type} -{self.name}'