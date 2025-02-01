from django.contrib import admin
from cars.models import Car,Brand #importar para parametro na hora do registro para aprecer no site

class BrandAdmin(admin.ModelAdmin):
    list_display =("name",)
    search_fields = ("name",)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value') #modelos que aparecerão no site
    search_fields = ('model','brand',) #filtragem no admin

admin.site.register(Car,CarAdmin) #registar as opções no site
admin.site.register(Brand,BrandAdmin) #registrar Brand 


