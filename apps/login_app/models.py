from __future__ import unicode_literals
from django.utils.datastructures import MultiValueDictKeyError

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

class Company(models.Model):
	company_name = models.CharField(max_length = 400, verbose_name=_("Company Name"), null=True)
	# invite_pin = models.CharField(max_length = 400, verbose_name=_("Invite Pin"), default=(current_pin))
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	invite_pin = models.SlugField(primary_key=True, unique=True, blank=True)
	def save(self, *args, **kwargs):
		while not self.invite_pin:
			ret = []
			ret.extend(random.sample(string.digits, 6))
			
			newslug = ''.join(ret)
			if not type(self).objects.filter(pk=newslug).count():
				self.invite_pin = newslug
				
		super(Company, self).save(*args, **kwargs)

	# class Meta:
	# 	abstract = True

	def __str__(self):
		return self.company_name


class UserManager(models.Manager):
	def registerVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['first_name']) < 3:
			results['status'] = False
			results['errors'].append('First Name must be at least 3 chars.')
		if len(postData['last_name']) < 3:
			results['status'] = False
			results['errors'].append('Last Name must be at least 3 chars.')
		if len(postData['invite_id']) < 5:
			results['status'] = False
			results['errors'].append('Please Enter Valid Invite Pin')
		if len(postData['user_rights']) < 5:
			results['status'] = False
			results['errors'].append('Error: Please Reload Page')
		if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
			results['status'] = False
			results['errors'].append('Please enter a valid email.')
		if len(postData['password']) < 4  or  postData['password'] != postData['c_password']:
			results['status'] = False
			results['errors'].append('Please enter a valid password.')

		#check to see if user is not in db
		user = User.objects.filter(email = postData['email'])
		# print (user, '*****', len(user))
		if len(user) >= 1:
			results['status'] = False
			results['errors'].append('User already exists!!!!')

		#checks to see if pin is valid
		pin = Company.objects.filter(invite_pin = postData['invite_id'])
		if len(pin) < 1:
			results['status'] = False
			results['errors'].append('Invalid Invite Pin')



		

		return results
	def createUser(self, postData):
		# p_hash = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
		p_hash = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
		# self.password_hash = p_hash.decode('utf8')
		user = User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], user_rights = postData['user_rights'], company=Company.objects.get(invite_pin = postData['invite_id']), email = postData['email'], password = p_hash)
		return user
	def loginVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		results['user'] = User.objects.filter(email = postData['email'])
		if len(results['user'] ) <1:
			results['status'] = False
			results['errors'].append('Something went wrong')
		else:
			# hashed = bcrypt.hashpw(postData['password'].encode('utf-8'), results['user'][0].password.encode('utf-8'))
			hashed = bcrypt.hashpw(postData['password'].encode('utf-8'), results['user'][0].password.encode('utf-8'))
			if hashed != results['user'][0].password:
				results['status'] = False
				results['errors'].append('Something went wrong')
		return results




class User(models.Model):
	first_name = models.CharField(max_length = 400, verbose_name=_("First Name"), null=True)
	last_name = models.CharField(max_length = 400, verbose_name=_("Last Name"), null=True)
	email = models.CharField(max_length = 400, verbose_name=_("Email"), null=True)
	password = models.CharField(max_length = 400, verbose_name=_("Password"), null=True)
	user_rights = models.CharField(_("User Rights"),max_length=256, choices=[('standard', 'Standard'), ('administrator', 'Administrator'), ('company_administrator', 'Company Administrator')])
	company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __str__(self):
		return self.first_name + " " + self.last_name