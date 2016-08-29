from django.contrib import admin

# Register your models here.

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('Year', 'Quarter', 'Date', 'Company', 'Revenues', 'EBIT', 'OperatingMargin', 
'Employees', 'RevenueperEmployee', 'EBITperEmployee', 'PPE', 'PPEperEmployee')

admin.site.register(Company, CompanyAdmin)

