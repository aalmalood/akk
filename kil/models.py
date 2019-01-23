from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=200)
    idd = models.CharField(max_length=200)
    
class Offers(models.Model):
    title = models.CharField(max_length=200)
    dest = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    agency = models.CharField(max_length=200)

class Customer(models.Model):
	phone = models.CharField(max_length=9)
	request = models.CharField(max_length=200)
	nppl = models.CharField(max_length=2)
	name = models.CharField(max_length=200)
	offer = models.CharField(max_length=5)


