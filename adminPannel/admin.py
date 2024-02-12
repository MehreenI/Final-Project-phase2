from django.contrib import admin
from .models import Product, FAQ, Category,Slider,Review



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','original_price','stock','description','short_description','image','category','is_featured','is_available')



class faqAdmin(admin.ModelAdmin):
    list_display = ('question','answer')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','image')


class SliderAdmin(admin.ModelAdmin):
    list_display = ('heading','image')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name','email','rating','comment')

admin.site.register(Slider, SliderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FAQ,faqAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Review,ReviewAdmin)




# Register your models here.
