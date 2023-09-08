from django.shortcuts import render, redirect, get_object_or_404
from shopApp.models import Product
from .models import Cart
from .models import CartItem
from  django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def addCart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save(),
    try:
        Cart_Items=CartItem.objects.get(product=product,cart=cart)
        if Cart_Items.quantity < Cart_Items.product.stock:
            Cart_Items.quantity += 1
            Cart_Items.save()
    except CartItem.DoesNotExist:
        Cart_Items = CartItem.objects.create(product=product, quantity=1,cart=cart)

        Cart_Items.save()
    return redirect('cart_app:cart_details')

def cart_details(request, total=0, counter=0, cart_items=None):
    try:

        cart=Cart.objects.get(cart_id=_cart_id(request))

        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter+=cart_item.quantity




    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))


def CartRemove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    Cart_Items = CartItem.objects.get(product=product, cart=cart)
    if Cart_Items.quantity > 1:
        Cart_Items.quantity -= 1
        Cart_Items.save()
    else:
        Cart_Items.delete()
    return redirect('cart_app:cart_details')
def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    Cart_Items = CartItem.objects.get(product=product, cart=cart)
    Cart_Items.delete()
    return redirect('cart_app:cart_details')






