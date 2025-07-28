from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render, redirect

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
    
class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 299.99},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 899.99},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 35.99},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 150.00}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            # Convert id to integer and validate range
            product_id = int(id)
            if product_id < 1 or product_id > len(Product.products):
                return HttpResponseRedirect(reverse('home'))
            
            product = Product.products[product_id - 1]
            viewData = {}
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product
            return render(request, self.template_name, viewData)
        except (ValueError, IndexError):
            # If id is not a valid integer or index is out of range
            return HttpResponseRedirect(reverse('home'))
        
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'
    success_template = 'products/success.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Get the next ID
            next_id = str(len(Product.products) + 1)
            
            # Create new product
            new_product = {
                "id": next_id,
                "name": form.cleaned_data['name'],
                "description": f"Description for {form.cleaned_data['name']}",
                "price": form.cleaned_data['price']
            }
            
            # Add to products list
            Product.products.append(new_product)
            
            # Show success page
            viewData = {}
            viewData["title"] = "Product Created Successfully"
            return render(request, self.success_template, viewData)
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)