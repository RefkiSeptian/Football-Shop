import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):       
    '''Product "mewarisi" dari models.Model jadi kita diwarisi sifat class tersebut
    yang ada method untuk mengakses/melakukan perubahan pada database jadi kita tidak perlu membuat methodnya lagi'''
    # Nama variable harus jelas dan bebas apa saja
    CATEGORY_CHOICES = [
        # pada baris berikut ini kita membuat tabel (meta data)
        ('jersey', 'Jersey'), # (value, display_name)
        ('boots', 'Football Boots'),
        ('ball', 'Football'),
        ('equipment', 'Equipment'),
        ('accessories', 'Accessories'),
        ('training', 'Training Gear'),
    ]
    
    # Field - field lain (atribut class)
    # Untuk liat tiap method ada parameter apa aja bisa dihover di atas method aja atau liat dokumentasi django
    price = models.DecimalField(max_digits=10,        # Total digit (termasuk desimal)
    decimal_places=2,                                   # Jumlah digit desimal  
    default=0.00,
    validators=[MinValueValidator(0)],   # Harga tidak boleh negatif
    verbose_name='Harga')

    # DATA: name
    # METADATA: CharField, max_length=255
    name = models.CharField(max_length=255) # Panjang maksimal 255
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category  = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False) 
    brand = models.CharField(max_length=225)
    stok = models.IntegerField(validators=[MinValueValidator(0)]) # Stok tidak boleh negatif
    
    def __str__(self):
        return self.name
    
    '''Ketika kita mengubah meta data (penambahan field, mengubah field,
    menambah model baru, perubahan relasi atau parameter) maka kita perlu
    melakukan migrasi ibarat kita melakukan renovasi rumah dan mengikuti 
    step step yang ada di formulir tetapi perubahan method, perubahan choice, 
    perubahan property itu tidak perlu melakukan migrasi'''
    
  