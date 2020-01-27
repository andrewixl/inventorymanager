from django.contrib import admin
from .models import Product, Location, userdepartment, usersub, active_header, Post
import data_wizard

# Register your models here.
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(userdepartment)
admin.site.register(usersub)
admin.site.register(active_header)

admin.site.register(Post)

# data_wizard.register(locations)
# data_wizard.register(users)
# data_wizard.register(product)