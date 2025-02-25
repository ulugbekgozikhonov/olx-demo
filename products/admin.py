from django.contrib import admin
from products.models import Advertisement, AdvertisementImage, Category


class AdvertisementImageInline(admin.TabularInline):  # yoki admin.StackedInline
    model = AdvertisementImage
    extra = 3  # Boshidan 3 ta rasm qo‘shish imkoniyati

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'status', 'seller')
    list_filter = ('category', 'status', 'is_new')
    search_fields = ('title', 'description')
    inlines = [AdvertisementImageInline]  # Rasmlar qo‘shish uchun Inline

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

admin.site.register(Advertisement, AdvertisementAdmin)

    