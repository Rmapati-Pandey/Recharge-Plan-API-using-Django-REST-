from django.contrib import admin
from api.models import Company,Plans
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name',)

class PlansAdmin(admin.ModelAdmin):
    list_display=('price','description','validity','data','sms','voice','company')
admin.site.register(Company,CompanyAdmin)
admin.site.register(Plans,PlansAdmin)