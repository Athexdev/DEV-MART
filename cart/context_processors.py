from .models import Cart

def cart(request):
    if request.user.is_authenticated:
        try:
            user_cart = Cart.objects.get(user=request.user)
            return {'cart': user_cart}
        except Cart.DoesNotExist:
            return {'cart': None}
    return {'cart': None}