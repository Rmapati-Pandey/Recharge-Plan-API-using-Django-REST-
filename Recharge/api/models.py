from django.db import models

# Create your models here.

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(primary_key=False,max_length=20)
    def __str__(self):
        return self.name

class Plans(models.Model):
    price= models.DecimalField(max_digits=10, decimal_places=2)     
    description=models.TextField(max_length=100)
    validity=models.TextField(max_length=25)
    data=models.CharField(max_length=20)
    sms=models.CharField(max_length=20, null=True)
    voice=models.CharField(max_length=20)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.description