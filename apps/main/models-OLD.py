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

class product(models.Model):
	manufacturer = models.CharField(max_length = 400, verbose_name=_("Manufacturer"), null=True)
	model = models.CharField(max_length = 400, verbose_name=_("Model"), null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.manufacturer + " " + self.model

class locations(models.Model):
    location = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.location

class students(models.Model):
	studentname = models.CharField(max_length=30)
	period = models.CharField(_("Period"),max_length=256, choices=[('1-2', 'Period 1/2'), ('3-4', 'Period 3/4'), ('4-5', 'Period 4/5'), ('5-6', 'Period 5/6')])
	studentid = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.studentname

class laptops(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	checkout = models.ForeignKey(students, on_delete=models.CASCADE)
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.inventory_id

class desktops(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class servers(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class accesspoints(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	checkout = models.ForeignKey(students, default='Not Checked Out', on_delete=models.CASCADE)
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class switches(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	speed = models.CharField(_("Speed"),max_length=256, choices=[('fast_ethernet', 'Fast Ethernet'), ('gigabit', 'Gigabit')])
	ports = models.CharField(_("Ports"),max_length=256, choices=[('8', '8-Ports'), ('24', '24-Ports'), ('48', '48-Ports')])
	poe = models.BooleanField()
	rack_units = models.CharField(_("Rack Units"),max_length=256, choices=[('1u', '1U'), ('2u', '2U'), ('3u', '3U'), ('4u', '4U')])
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class routers(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	speed = models.CharField(_("Speed"),max_length=256, choices=[('fast_ethernet', 'Fast Ethernet'), ('gigabit', 'Gigabit')])
	ports = models.CharField(_("Ports"),max_length=256, choices=[('8', '8-Ports'), ('24', '24-Ports'), ('48', '48-Ports')])
	poe = models.BooleanField()
	rack_units = models.CharField(_("Rack Units"),max_length=256, choices=[('1u', '1U'), ('2u', '2U'), ('3u', '3U'), ('4u', '4U')])
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class asas(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	speed = models.CharField(_("Speed"),max_length=256, choices=[('fast_ethernet', 'Fast Ethernet'), ('gigabit', 'Gigabit')])
	ports = models.CharField(_("Ports"),max_length=256, choices=[('8', '8-Ports'), ('24', '24-Ports'), ('48', '48-Ports')])
	poe = models.BooleanField()
	rack_units = models.CharField(_("Rack Units"),max_length=256, choices=[('1u', '1U'), ('2u', '2U'), ('3u', '3U'), ('4u', '4U')])
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	checkout = models.ForeignKey(students, on_delete=models.CASCADE)
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class paloaltos(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	checkout = models.ForeignKey(students, on_delete=models.CASCADE)
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class junipers(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	checkout = models.ForeignKey(students, on_delete=models.CASCADE)
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class wirelessadapters(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	speed = models.CharField(max_length = 400, verbose_name=_("Speed"), null=True)
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	checkout = models.ForeignKey(students, on_delete=models.CASCADE)
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class ssd(models.Model):
	owner_company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	inventory_id = models.CharField(max_length = 400, verbose_name=_("Company ID"), null=True)	
	product = models.ForeignKey(product, on_delete=models.CASCADE)
	size = models.CharField(max_length = 400, verbose_name=_("Size"), null=True)
	status = models.CharField(_("Status"),max_length=256, choices=[('active', 'Active'), ('stored', 'Stored'), ('checked out', 'Checked Out')])
	checkout = models.ForeignKey(students, on_delete=models.CASCADE)
	location = models.ForeignKey(locations, on_delete=models.CASCADE)
	serial_number = models.CharField(max_length = 400, verbose_name=_("Serial Number"), null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.company_id

class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title 	