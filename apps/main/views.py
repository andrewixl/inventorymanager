from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import locations, students, laptops, desktops, servers, accesspoints, switches, routers, asas, paloaltos, junipers, wirelessadapters, ssd, product

import json
from urllib.request import urlopen

# Create your views here.
def index(request):
   try:
      request.session['user_id']
   except KeyError:
      return redirect("/signin")
   user = User.objects.get(id = request.session['user_id'])
   print (user.user_rights)
   context = {
      "user" : user,
   }
   return render(request, 'main/index.html', context)

def profile(request):
   try:
      request.session['user_id']
   except KeyError:
      return redirect("/signin")
   user = User.objects.get(id = request.session['user_id'])
   context = {
      "user" : user,
   }
   return render(request, 'main/profile.html', context)

def inventory(request,id):
   try:
      request.session['user_id']
   except KeyError:
      return redirect("/signin")

   response = urlopen('http://localhost:8000/static/main/ajax/tableheaders.json')
   data = json.load(response)
   jsondata = {}
   for key, value in data.items():
      jsondata[key] = value
   headers = []
   headers = jsondata[id]

   title = id.capitalize()

   user = User.objects.get(id = request.session['user_id'])
   inventory = eval(id).objects.filter (owner_company = user.company).all()
   context = {
      "id" : id,
      "title" : title,
      "user" : user,
      "headers" : headers,
      "inventory" : inventory,
   }
   return render(request, 'main/inventory.html', context)

def checkedout(request,id):
   try:
      request.session['user_id']
   except KeyError:
      return redirect("/signin")

   response = urlopen('http://localhost:8000/static/main/ajax/tableheaders.json')
   data = json.load(response)
   jsondata = {}
   for key, value in data.items():
      jsondata[key] = value
   headers = []
   headers = jsondata[id]

   title = id.capitalize()

   user = User.objects.get(id = request.session['user_id'])
   inventory = eval(id).objects.filter (owner_company = user.company, status = "checked out").all()
   context = {
      "id" : id,
      "title" : title,
      "user" : user,
      "headers" : headers,
      "inventory" : inventory,
   }
   return render(request, 'main/inventory.html', context)