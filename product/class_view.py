from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CreateProductForm, UpdateProductForm
from .models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'products/home.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name =  'products/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/create_product.html'
    form_class = CreateProductForm
    context_object_name = 'product_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    form_class = UpdateProductForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    pk_url_kwarg = 'id'

    def get_context_data(self):
        return reverse('home')