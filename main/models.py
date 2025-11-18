import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Product(models.Model):       
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
        ('others', 'Other things'),
    ]
    
    # Field - field lain (atribut class)
    # Untuk liat tiap method ada parameter apa aja bisa dihover di atas method aja atau liat dokumentasi django
    price = models.DecimalField(max_digits=10,        # Total digit (termasuk desimal)
    decimal_places=1,                                   # Jumlah digit desimal  
    default=0.0,
    validators=[MinValueValidator(0)],   # Harga tidak boleh negatif
    verbose_name='Harga')

    # DATA: name
    # METADATA: CharField, max_length=255
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) # Panjang maksimal 255
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category  = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False) 
    brand = models.CharField(max_length=225)
    stok = models.IntegerField(validators=[MinValueValidator(0)]) # Stok tidak boleh negatif
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.name
    
    '''Ketika kita mengubah meta data (penambahan field, mengubah field,
    menambah model baru, perubahan relasi atau parameter) maka kita perlu
    melakukan migrasi ibarat kita melakukan renovasi rumah dan mengikuti 
    step step yang ada di formulir tetapi perubahan method, perubahan choice, 
    perubahan property itu tidak perlu melakukan migrasi'''
    
  