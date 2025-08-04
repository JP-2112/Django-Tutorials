from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.core.exceptions import ValidationError

class homePageView(TemplateView):
    template_name = 'pages/home.html'

class aboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'About us - Online Store',
            'subtitle': 'About us',
            'description': 'This is an about page...',
            'author': 'Developed by: Juan Pablo Corena'
        })
        return context

class contactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Contact Us - Online Store',
            'subtitle': 'Contact Information',
            'email': 'info@onlinestore.com',
            'address': 'Mall Viva Envigado, local 123, Envigado, Colombia',
            'phone': '+57 300 123 4567'
        })
        return context

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.objects.all()
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product id must be 1 or greater")
            product = get_object_or_404(Product, pk=product_id)
            
            viewData = {}
            viewData["title"] = product.name + " - Online Store"
            viewData["subtitle"] = product.name + " - Product information"
            viewData["product"] = product

            return render(request, self.template_name, viewData)
        except (ValueError, IndexError):
            return HttpResponseRedirect(reverse('home'))
        
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Products - Online Store"
        context['subtitle'] = "List of products"
        return context

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError('Price must be greater than zero.')
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)