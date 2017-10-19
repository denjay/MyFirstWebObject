from django.shortcuts import render
from df_user import user_decorator
from .models import CartInfo


@user_decorator.login
def cart(request):
    user_id = request.session.get('user_id')
    items = CartInfo.objects.filter(user=user_id)
    print(items)
    context = {"items": items, "title": '购物车'}
    return render(request, 'df_cart/cart.html', context)
