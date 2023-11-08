from django.shortcuts import render
from django.views.generic import View
from django.views import View
from .models import Product,Customer,Cart
from .forms import CustomerRegistrationForm, CustomerProfileForm

from django.contrib import messages

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        traditional = Product.objects.filter(category='T')
        western = Product.objects.filter(category='W')

        return render(request, 'app/home.html', {'laptop': laptop, 'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'traditional': traditional, 'western':western})

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})

# def add_to_cart(request):
#     user=request.user
#     product_id=request.GET.get('prod_id')
#     product=product.objects.get(product_id)
#     Cart(user=user , product=product).save()
#     return render(request, 'app/addtocart.html')


from django.shortcuts import render, redirect
from .models import Product, Cart

from django.shortcuts import render, redirect
from .models import Product, Cart

def add_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('prod_id')

        try:
            product = Product.objects.get(pk=product_id)
            Cart.objects.create(user=user, product=product)
            messages.success(request, 'Product added to cart successfully')
        except Product.DoesNotExist:
            messages.error(request, 'Product not found')

        return redirect('cart')  # Redirect to the cart page or another appropriate URL
    else:
        messages.warning(request, 'Please log in to add products to your cart')
        return redirect('login')  # Redirect to the login page or another appropriate URL


from django.shortcuts import render
from .models import Product




def buy_now(request):
    return render(request, 'app/buynow.html')


def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add})

def orders(request):
    return render(request, 'app/orders.html')

def mobile(request, data=None):
    mobiles = Product.objects.none()
    if data == 'all':
        mobiles = Product.objects.filter(category='M')
    elif data == 'Redmi' or data == 'Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discount_price__gte=10000)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discount_price__lt=10000)

    return render(request, 'app/mobile.html', {'mobiles': mobiles})

def laptop(request, data=None):
    laptops = Product.objects.none()
    if data == 'all':
        laptops = Product.objects.filter(category='L')
    elif data == 'hp' or data == 'lenovo' or data == 'dell' or data == 'asus':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'above':
        laptops = Product.objects.filter(category='L').filter(discount_price__gte=60000)
    elif data == 'below':
        laptops = Product.objects.filter(category='L').filter(discount_price__lt=60000)

    return render(request, 'app/laptop.html', {'laptops': laptops})

def topwear(request, data=None):
    topwear = Product.objects.none()
    if data == 'all':
        topwear = Product.objects.filter(category='TW')
    elif data == 'zara' or data == 'reymond':
        topwear = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'above':
        topwear = Product.objects.filter(category='TW').filter(discount_price__gte=200)
    elif data == 'below':
        topwear = Product.objects.filter(category='TW').filter(discount_price__lt=200)

    return render(request, 'app/topwear.html', {'topwear': topwear})

def bottomwear(request, data=None):
    bottomwear = Product.objects.none()
    if data == 'all':
        bottomwear = Product.objects.filter(category='BW')
    elif data == 'denim':
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'above':
        bottomwear = Product.objects.filter(category='BW').filter(discount_price__gte=300)
    elif data == 'below':
        bottomwear = Product.objects.filter(category='BW').filter(discount_price__lt=300)

    return render(request, 'app/bottomwear.html', {'bottomwear': bottomwear})

def traditional(request, data=None):
    traditional = Product.objects.none()
    if data == 'all':
        traditional = Product.objects.filter(category='T')
    elif data == 'layra' or data == 'HandM':
        traditional = Product.objects.filter(category='T').filter(brand=data)
    elif data == 'above':
        traditional = Product.objects.filter(category='T').filter(discount_price__gte=1000)
    elif data == 'below':
        traditional = Product.objects.filter(category='T').filter(discount_price__lt=1000)

    return render(request, 'app/traditional.html', {'traditional': traditional})

def western(request, data=None):
    western = Product.objects.none()
    if data == 'all':
        western = Product.objects.filter(category='W')
    elif data == 'unique' or data == 'wordplay':
        western = Product.objects.filter(category='W').filter(brand=data)
    elif data == 'above':
        western = Product.objects.filter(category='W').filter(discount_price__gte=500)
    elif data == 'below':
        western = Product.objects.filter(category='W').filter(discount_price__lt=500)

    return render(request, 'app/western.html', {'western': western})

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registration successful')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})

def checkout(request):
    return render(request, 'app/checkout.html')

from django.views.generic import View
from django.shortcuts import render
from .forms import CustomerProfileForm
from .models import Customer

class ProfileView(View):
    template_name = 'app/profile.html'  # Define the correct template_name
    active = 'btn-primary'  # Define the 'active' attribute

    def get(self, request):
        form = CustomerProfileForm()  # Instantiate the form
        return render(request, self.template_name, {'form': form, 'active': self.active})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile updated successfully')
        return render(request, self.template_name, {'form': form, 'active': self.active})

