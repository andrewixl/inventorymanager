from django.contrib import admin
from .models import User, Company
# from .functions import Security

# Register your models here.
admin.site.register(User)
# admin.site.register(Company)

@admin.register(Company)
class Apparel_ProductAdmin(admin.ModelAdmin):
    # Security.getpin()
    save_on_top = True
    fields = ["company_name", "invite_pin"]
    readonly_fields = ["invite_pin"]