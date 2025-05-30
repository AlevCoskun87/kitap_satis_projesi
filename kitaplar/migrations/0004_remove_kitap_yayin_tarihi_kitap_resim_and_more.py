# Generated by Django 5.2.1 on 2025-05-17 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitaplar', '0003_alter_kitap_options_remove_kitap_aciklama_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitap',
            name='yayin_tarihi',
        ),
        migrations.AddField(
            model_name='kitap',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to='kitap_resimleri/'),
        ),
        migrations.AlterField(
            model_name='kitap',
            name='isim',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='kitap',
            name='yazar',
            field=models.CharField(max_length=100),
        ),
    ]
