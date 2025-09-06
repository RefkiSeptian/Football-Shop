from django.shortcuts import render


def show_main(request):
    context = {
        'nama_produk' : 'Manchester United Home Jersey 2024',
        'brand': 'Brand: Adidas',
        'deskripsi': 'Jersey kandang Manchester United musim 2024/2025 dengan teknologi AEROREADY untuk performa maksimal.',
        'harga' : 'Rp 899.000',
        'stok' : 'Stok: 25',

    }

    return render(request, "main.html", context)