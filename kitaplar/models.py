from django.db import models
from django.contrib.auth.models import User

class Kitap(models.Model):
    baslik = models.CharField(max_length=200)
    yazar = models.CharField(max_length=100)
    fiyat = models.DecimalField(max_digits=6, decimal_places=2)
    resim = models.ImageField(upload_to='kitap_resimleri/')

    def __str__(self):
        return self.baslik

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kitap = models.ForeignKey(Kitap, on_delete=models.CASCADE)
    adet = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.kitap.baslik} - {self.adet} adet"
