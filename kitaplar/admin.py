from django.contrib import admin
from .models import Kitap, CartItem

@admin.register(Kitap)
class KitapAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yazar', 'fiyat')  # 'yazar' modeli var, kullanılabilir
    search_fields = ('baslik', 'yazar')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('kitap', 'adet')
