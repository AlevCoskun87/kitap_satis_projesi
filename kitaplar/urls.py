from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    # urls.py
    path('sepet/ekle/<int:kitap_id>/', views.sepete_ekle, name='sepete_ekle'),
    path('sepetim/', views.sepetim, name='sepetim'),
    path('sepet/arttir/<int:item_id>/', views.adet_arttir, name='adet_arttir'),
    path('sepet/azalt/<int:item_id>/', views.adet_azalt, name='adet_azalt'),
    path('sepet/sil/<int:item_id>/', views.sepetten_sil, name='sepetten_sil'),

    path('kayit/', views.kayit_ol, name='kayit_ol'),
    path('giris/', views.giris_yap, name='giris_yap'),
    path('cikis/', LogoutView.as_view(next_page='/giris/'), name='logout'),

    path('odeme/', views.odeme_yap, name='odeme_yap'),
    path('odeme/basarili/', views.odeme_basarili, name='odeme_basarili'),

    
]
