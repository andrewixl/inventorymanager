from django.contrib import admin
from .models import locations, students, laptops, desktops, servers, accesspoints, switches, routers, asas, paloaltos, junipers, wirelessadapters, ssd, product
import data_wizard

# Register your models here.
admin.site.register(laptops)
admin.site.register(desktops)
admin.site.register(servers)
admin.site.register(accesspoints)
admin.site.register(switches)
admin.site.register(routers)
admin.site.register(asas)
admin.site.register(paloaltos)
admin.site.register(junipers)
admin.site.register(wirelessadapters)
admin.site.register(ssd)




admin.site.register(locations)
admin.site.register(students)
admin.site.register(product)

data_wizard.register(students)