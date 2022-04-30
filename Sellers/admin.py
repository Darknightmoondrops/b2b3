from django.contrib import admin
from .models import SellersCategories,Sellers

@admin.register(SellersCategories)
class SellersCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
@admin.register(Sellers)
class SellersAdmin(admin.ModelAdmin):
    list_display = ['business_name','registration_date','business_status']
    search_fields = ['business_name','registration_date']
    


