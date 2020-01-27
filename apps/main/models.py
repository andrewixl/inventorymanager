from __future__ import unicode_literals
from django.utils.datastructures import MultiValueDictKeyError
from ..login_app.models import Company

from django.db import models
import re
import bcrypt
from django import forms
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# from .functions import Security
# from .functions import current_pin


import string, random

# Create your models here.

class Product(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("company"), on_delete=models.CASCADE)
	manufacturer = models.CharField(max_length = 400, verbose_name=_("Manufacturer"), null=True)
	model = models.CharField(max_length = 400, verbose_name=_("Model"), null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.manufacturer + " " + self.model

class Location(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("company"), on_delete=models.CASCADE)
	location = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.location

class userdepartment(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("company"), on_delete=models.CASCADE)
	userdepartment = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.userdepartment

class usersub(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("company"), on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	department = models.ForeignKey(userdepartment, verbose_name=_("department"), on_delete=models.CASCADE)
	studentid = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.first_name + self.last_name

class active_header(models.Model):
	inventory_id = models.BooleanField()
	product = models.BooleanField()
	size = models.BooleanField()
	speed = models.BooleanField()
	ports = models.BooleanField()
	poe = models.BooleanField()
	rack_units = models.BooleanField()
	status = models.BooleanField()
	checkout = models.BooleanField()
	location = models.BooleanField()
	serial_number = models.BooleanField()
	created_at = models.BooleanField()
	updated_at = models.BooleanField()

class Post(models.Model):
	location = models.CharField(max_length=30)
