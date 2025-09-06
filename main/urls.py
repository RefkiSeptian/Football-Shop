from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    # Parameter pertama untuk path page yang ingin kita tampilkan
    # Parameter kedua adalah function pada view

    path('', show_main, name='show_main'),
]