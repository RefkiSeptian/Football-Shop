from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):

    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'name' : 'Refki Septian', 
        'npm' : '2406397196', 
        'class' : 'PBP C', 
        'product_list' : product_list, 
        'last_login': request.COOKIES.get('last_login', 'Never'),

    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_detail_product(request, id):
    product = get_object_or_404(Product, pk=id)
   
    context = {
        'product': product
    }

    return render(request, "show_detail_product.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list) # translate menjadi xml
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),  # UUID string
            'name': product.name,
            'price': float(product.price),  
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'stok': product.stok,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, news_id):
   try:
       product_item = Product.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': float(product.price),
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'stok': product.stok,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        # Jika request dari AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if form.is_valid():
                form.save()
                return JsonResponse({"status": "success", "message": "Akun berhasil dibuat!"})
            else:
                # Ambil error pertama
                error_message = next(iter(form.errors.values()))[0]
                return JsonResponse({"status": "error", "message": error_message}, status=400)

        # Jika bukan AJAX → fallback redirect biasa
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')

    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # Jika request dari AJAX (fetch)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = JsonResponse({"status": "success", "message": "Login berhasil!"})
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                error_message = list(form.errors.values())[0][0]
                return JsonResponse({"status": "error", "message": error_message}, status=401)

        # Fallback kalau bukan AJAX (langsung redirect seperti biasa)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

# def login_user(request):
#    if request.method == 'POST':
#       form = AuthenticationForm(data=request.POST) # Kasih formulir kosong untuk login 

#       if form.is_valid():
#         user = form.get_user()  # cari user dengan username bla bla di data base dan check apakah passwordnya sama dengan yang dimasukkan di formulir
#         login(request, user)
#         response = HttpResponseRedirect(reverse("main:show_main"))
#         response.set_cookie('last_login', str(datetime.datetime.now()))
#         return response

#    else:
#       form = AuthenticationForm(request)
#    context = {'form': form}
#    return render(request, 'login.html', context)

# def logout_user(request):
#     logout(request)
#     response = HttpResponseRedirect(reverse('main:login'))
#     response.delete_cookie('last_login')
#     return response

def logout_user(request):
    logout(request)

    # Hapus cookie 
    response_redirect = redirect('main:login')
    response_redirect.delete_cookie('last_login')

    # Jika request dari AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({"status": "success", "message": "Berhasil logout!"})

    # Jika access biasa via link
    messages.success(request, "Berhasil logout!")
    return response_redirect

@csrf_exempt
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"}, status=200)
        return JsonResponse({"status": "error", "errors": form.errors}, status=400)

    # fallback kalau bukan AJAX
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    return render(request, "edit_product.html", {"form": form})

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()

    # Jika request dari AJAX
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"status": "success"})

    # Jika request dari form biasa, fallback ke redirect
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    brand = request.POST.get("brand")
    price = request.POST.get("price")
    stok = request.POST.get("stok")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    description = request.POST.get("description")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user  

    new_product = Product(
        name=name,
        brand=brand,
        price=price,
        stok=stok,
        category=category,
        thumbnail=thumbnail,
        description=description,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)