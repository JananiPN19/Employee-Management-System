from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=255)
    phone_num = models.CharField(max_length=12)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    address = models.TextField()
    job = models.ManyToManyField('AvailableJob',blank=True)
    dob = models.DateField()

class AvailableJob(models.Model):
    job_name = models.CharField(max_length=50)

    def __str__(self):
        return self.job_name
