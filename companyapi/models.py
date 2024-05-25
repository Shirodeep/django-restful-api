from django.db import models

gender_choice = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
]
class CompanyUsers(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices=gender_choice, default='M', max_length=1)
    description = models.TextField(blank=True)