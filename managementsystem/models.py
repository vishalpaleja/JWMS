from django.db import models
# from adaptor.model import CsvModel
# from adaptor.fields import CharField, DateField

# Create your models here.
class Inbound(models.Model):
	timestamp = models.DateField(auto_now= True)
	trackingNumber = models.CharField(max_length=100)
	customer = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	outboundTracking = models.CharField(max_length=100)
	service = models.CharField(max_length=100)
	note = models.CharField(max_length=100)