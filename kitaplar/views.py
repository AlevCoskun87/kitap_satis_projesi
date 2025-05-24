from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Kitap, CartItem
from django.contrib import messages

def anasayfa(request):
    kitaplar = Kitap.objects.all()
    return render(request, 'kitaplar/anasayfa.html', {'kitaplar': kitaplar})

@login_required
def sepete_ekle(request, kitap_id):
    kitap = get_object_or_404(Kitap, id=kitap_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, kitap=kitap)
    if not created:
        cart_item.adet += 1
        cart_item.save()
    messages.success(request, f"{kitap.baslik} sepete eklendi.")
    return redirect('anasayfa')

@login_required
def sepetim(request):
    sepet_urunleri = CartItem.objects.filter(user=request.user)

    # Her ürün için toplam fiyatı hesapla
    for item in sepet_urunleri:
        item.toplam = item.adet * item.kitap.fiyat

    toplam_fiyat = sum(item.toplam for item in sepet_urunleri)

    return render(request, 'kitaplar/sepet.html', {
        'sepet_urunleri': sepet_urunleri,
        'toplam_fiyat': toplam_fiyat
    })

@login_required
def adet_arttir(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.adet += 1
    item.save()
    return redirect('sepetim')

@login_required
def adet_azalt(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.adet > 1:
        item.adet -= 1
        item.save()
    else:
        item.delete()
    return redirect('sepetim')

@login_required
def sepetten_sil(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('sepetim')

def kayit_ol(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('anasayfa')
    else:
        form = UserCreationForm()
    return render(request, 'kitaplar/kayit.html', {'form': form})

def giris_yap(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('anasayfa')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

from django.shortcuts import redirect

@login_required
def odeme_yap(request):
    sepet_urunleri = CartItem.objects.filter(user=request.user)
    toplam = sum(item.adet * item.kitap.fiyat for item in sepet_urunleri)

    if request.method == 'POST':
        odeme_yontemi = request.POST.get('odeme_yontemi')
        
        # Burada ödeme yöntemi kontrolü yapılabilir
        if odeme_yontemi not in ['kredi_karti', 'havale', 'kapida_odeme']:
            messages.error(request, "Geçersiz ödeme yöntemi seçtiniz.")
            return redirect('odeme_yap')
        
        # Ödeme başarılı simülasyonu
        # Sepeti temizle
        sepet_urunleri.delete()

        # Ödeme yöntemini başarı sayfasına taşıyabiliriz (opsiyonel)
        request.session['odeme_yontemi'] = odeme_yontemi
        
        return redirect('odeme_basarili')
    
    return render(request, 'kitaplar/odeme.html', {'toplam': toplam})




@login_required
def odeme_basarili(request):
    return render(request, 'kitaplar/odeme_basarili.html')