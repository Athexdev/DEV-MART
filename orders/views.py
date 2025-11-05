from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.http import require_POST
import stripe
from cart.models import Cart, CartItem
from .models import Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    if not cart.items.exists():
        return redirect('view_cart')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        
        total_amount = cart.get_total()
        
        order = Order.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            postal_code=postal_code,
            country=country,
            total_amount=total_amount,
            payment_method='stripe',
        )
        
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
        
        return redirect('payment', order_id=order.id)
    
    context = {
        'cart': cart,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        
        try:
            charge = stripe.Charge.create(
                amount=int(order.total_amount * 100),
                currency='usd',
                source=token,
                description=f'Order #{order.id}',
            )
            
            order.payment_status = 'completed'
            order.status = 'confirmed'
            order.save()
            
            Cart.objects.get(user=request.user).items.all().delete()
            
            return redirect('order_confirmation', order_id=order.id)
        except stripe.error.CardError as e:
            context = {
                'order': order,
                'error': e.user_message,
                'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            }
            return render(request, 'orders/payment.html', context)
    
    context = {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'orders/payment.html', context)


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {
        'order': order,
    }
    return render(request, 'orders/order_confirmation.html', context)


@login_required
def order_list(request):
    orders = request.user.orders.all()
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {
        'order': order,
    }
    return render(request, 'orders/order_detail.html', context)