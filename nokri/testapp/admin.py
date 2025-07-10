from django.contrib import admin
from testapp.models import Mumbai, Pune, Hyderabad
# Register your models here.


class MumbaiAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'job_titles', 'sal', 'qualifications', 'joining_date', 'location', 'address']    
    
admin.site.register(Mumbai, MumbaiAdmin)

class PuneAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'job_titles', 'sal', 'qualifications', 'joining_date', 'location', 'address']
    
admin.site.register(Pune, PuneAdmin)

class HyderabadAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'job_titles', 'sal', 'qualifications', 'joining_date', 'location', 'address']    
    
admin.site.register(Hyderabad, HyderabadAdmin)