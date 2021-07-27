from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateProductForm, UpdateProductForm
from .models import *

def home_page(request):
    cotegories=Category.objects.all()
    # print(cotegories)

    #SELECT * from category
    return render(request, 'products/home.html', {'cotegories': cotegories})

def product_list(request,slug):
    products=Product.objects.filter(category__slug=slug)
    return  render(request,'products/list.html', {'products':products})

def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request ,'products/detail.html',{'product':product})

def create_product(request):
    if request.method=='POST':
        # print(request.POST)
        product_form = CreateProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            return redirect(product.get_absolute_url())
    else:
        product_form=CreateProductForm()
    return render(request,'products/create_product.html', {'product_form':product_form})

def update_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product_form = UpdateProductForm(request.POST or None, request.FILES or None,
                                     instance=product)
    if product_form.is_valid():
        product_form.save()
        return redirect(product.get_absolute_url())
    return render(request, 'products/update_product.html',
                  {'product_form':product_form})

def delete_product(request,id):
    product = get_object_or_404(Product, pk=id)
    if request.method =='POST':
        slug=product.category.slug
        product.delete()
        return redirect('list', slug)
    return render(request, 'products/delete_product.html', {'product': product})

