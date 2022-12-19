from django.db import models

# Create your models here.
class Plan(models.Model):
    validity = models.IntegerField()
    data= models.FloatField()
    price=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class RechagreHistory(models.Model):
    mobile_number = models.CharField(max_length=10)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    

    

