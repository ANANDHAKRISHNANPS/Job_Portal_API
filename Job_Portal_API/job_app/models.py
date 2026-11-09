from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JobModel(models.Model):
    job_title=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    job_description=models.TextField()
    location=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=20,decimal_places=2)
    job_type=models.CharField(max_length=50)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='jobs',null=True)
