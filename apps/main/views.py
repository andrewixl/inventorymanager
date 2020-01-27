from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Location, usersub, Product, Post

from django.http import JsonResponse
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
   # inventory = eval(id).objects.filter (owner_company = user.company).all()
   product = Product.objects.filter (owner_company = user.company).all()
   location_data = Location.objects.filter (owner_company = user.company).all()
   context = {
      "id" : id,
      "title" : title,
      "user" : user,
      "headers" : headers,
      "inventory" : inventory,
      "product" : product,
      "location" : location_data,
   }

   locations = Location.objects.filter (owner_company = user.company).all()
   response_data = {}
   if request.POST.get('action') == 'post':
      location = request.POST.get('location')

      response_data['location'] = location
      
      Location.objects.create(
         owner_company = user.company,
         location = location,
      )
      return JsonResponse(response_data)

      
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
   # inventory = eval(id).objects.filter (owner_company = user.company, status = "checked out").all()
   context = {
      "id" : id,
      "title" : title,
      "user" : user,
      "headers" : headers,
      "inventory" : inventory,
   }
   return render(request, 'main/inventory.html', context)

def create_post(request):
   # posts = Post.objects.all()
   # response_data = {}

   # if request.POST.get('action') == 'post':
   #    title = request.POST.get('title')
   #    description = request.POST.get('description')

   #    response_data['title'] = title
   #    response_data['description'] = description
      
   #    Post.objects.create(
   #       title = title,
   #       description = description,
   #    )
   #    return JsonResponse(response_data)

   # return render(request, 'main/create_post.html', {'posts':posts})   
   return render(request, 'main/create_post.html')


   # def create_post(request):
   # posts = Post.objects.all()
   # response_data = {}

   # if request.POST.get('action') == 'post':
   #    title = request.POST.get('title')
   #    description = request.POST.get('description')

   #    response_data['title'] = title
   #    response_data['description'] = description
      
   #    Post.objects.create(
   #       title = title,
   #       description = description,
   #    )
   #    return JsonResponse(response_data)

   # return render(request, 'main/create_post.html', {'posts':posts})  