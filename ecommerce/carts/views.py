from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from orders.models import Order
from django.contrib.auth.decorators import login_required
from home.forms import LoginForm, GuestForm
from home.models import GuestEmail
from billing.models import BillingProfile
# Create your views here.

def cart_home_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request,'carts/cart_home.html',{"cart":cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print('Product not avilable...')
            return redirect('carts:home')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_item'] = cart_obj.products.count()
        # return redirect(product_obj.get_absolute_url())
    return redirect('carts:home')


def checkout_view(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("carts:home")
    else:
        order_obj,new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    user = request.user
    billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')
    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create( email=guest_email_obj.email)
    else:
        pass
    context={
        "object":order_obj,
        "billing_profile":billing_profile,
        "login_form":login_form,
        "guest_form":guest_form
    }

    return render(request, 'carts/checkout.html',context)
