from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __str__(self):
        return"{}_token".format(self.user)

class Available_Public_IP(models.Model):
    IP = models.CharField(max_length=255, null=True)  
    date_start = models.DateTimeField(null=True, blank=True)
    date_expire = models.DateTimeField(null=True, blank=True)
    price_bought = models.BigIntegerField(null=True, blank=True)
    price_to_sell = models.BigIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return "IP :{}-will expire on {}".format(self.IP, self.date_expire)

class Used_Public_IP(models.Model):
    IP = models.CharField(max_length=255, null=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_expire = models.DateTimeField(null=True, blank=True)
    price_bought = models.BigIntegerField(null=True, blank=True)
    price_sold = models.BigIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return "IP :{}-will expire on {}".format(self.IP, self.date_expire)

class Used_Private_IP(models.Model):
    IP = models.CharField(max_length=255, null=True) 
    Device = models.CharField(max_length=255, null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_expire = models.DateTimeField(null=True, blank=True)
    price_bought = models.BigIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return "IP :{}-will expire on {}".format(self.IP, self.date_expire)