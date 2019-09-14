from django.db import models

# Create your models here.

class orderDetails_db(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    rollNo = models.IntegerField();
    itemName = models.CharField(max_length = 100)
    company = model.CharField(max_length=1, choices=[
        'zomato':'Zomato',
        'swiggy' : 'Swiggy',
        'other' : 'other',
    ])
    deliveryGuyContact = model.IntegerField();

    def __str__(self):
        return self.rollNo
