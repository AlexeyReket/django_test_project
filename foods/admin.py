from django.contrib import admin

from foods.models import Food, FoodCategory


# Register your models here.
class FoodCategoryAdmin(admin.ModelAdmin):
    pass


class FoodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
