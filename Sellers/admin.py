from django.contrib import admin
from .models import VendorCategories,Sellers

@admin.register(VendorCategories)
class VendorCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name','status']
    search_fields = ['name']
    
@admin.register(Sellers)
class SellersAdmin(admin.ModelAdmin):
    list_display = ['business_name','registration_date','business_status']
    search_fields = ['business_name','registration_date']
    


