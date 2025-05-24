# 📚 Kitap Sepeti

Kitap Sepeti, Django framework’ü ve Djongo aracılığıyla MongoDB veritabanı ile geliştirilen basit bir kitap satış uygulamasıdır. Bu uygulama, kullanıcıların kitapları görüntüleyip sepetlerine eklemelerine ve basit bir ödeme süreciyle siparişlerini tamamlamalarına olanak tanır.

## 🚀 Özellikler

- Kitap listeleme
- Kitapları sepete ekleme
- Sepet içeriğini güncelleme ve silme
- Ödeme ekranı (simülasyon)
- Kullanıcı girişi ve oturum yönetimi
- Django admin paneli ile içerik yönetimi

## 🛠 Kullanılan Teknolojiler

- Python 3.x
- Django 4.x
- Djongo (MongoDB desteği için)
- MongoDB (veritabanı)
- HTML, CSS, Bootstrap (arayüz tasarımı)
- VS Code (geliştirme ortamı)

## ⚙️ Kurulum

### 1. Depoyu Klonlayın (veya ZIP ile açın)

```bash
git clone https://github.com/kullaniciadi/kitap-sepeti.git
cd kitap-sepeti
```

### 2. Gereksinimleri Yükleyin

```bash
pip install -r requirements.txt
```

### 3. Veritabanı Ayarlarını Yapın (`settings.py`)

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'kitapsepeti_db',
    }
}
```

### 4. Sunucuyu Başlatın

```bash
python manage.py runserver
```

## 🖼 Ekran Görüntüleri

| Sayfa         | Açıklama                                        |
|---------------|--------------------------------------------------|
| Ana Sayfa     | Kitap listesi ve “Sepete Ekle” butonları        |
| Giriş Sayfası | Kullanıcı adı / şifre ekranı                     |
| Sepetim       | Kitap adedi ve toplam tutar                     |
| Ödeme         | Ödeme yöntemi seçimi                            |
| Sonuç         | “Ödeme başarılı” ekranı                         |

## 👤 Geliştirici

- **Adı Soyadı**: Alev Coşkun  
- **Teslim Tarihi**: 30 Mayıs 2025  
- **Ders**: Python Uygulama Geliştirme


