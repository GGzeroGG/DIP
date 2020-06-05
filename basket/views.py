from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForBasket

def basket_add(request):
#    messages.success(request, 'Товар добавлен в корзину')
    return_dict = dict()

    data = request.POST
    product_id = data.get("product_id")
    quantity_nbr = data.get("quantity_nbr")
    is_delete = data.get("is_delete")
        
#    if int(quantity_nbr) > Product.objects.get(id=product_id).warehouse:
#        messages.error(request, 'Ошибка количества')
##        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
#        pass
#    else:
    if is_delete == 'true':
        ProductsInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductsInBasket.objects.get_or_create(user=request.user, product_id=product_id, is_active=True, defaults={"quantity_nbr":quantity_nbr }  )
        if not created:
            new_product.quantity_nbr += int(quantity_nbr)
            new_product.save(force_update=True)


    products_in_basket = ProductsInBasket.objects.filter(user=request.user, is_active=True)
    product_total_quantity_nbr = products_in_basket.count()  
    return_dict["product_total_quantity_nbr"] = product_total_quantity_nbr

    return_dict["products"] = list()
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["quantity_nbr"] = item.quantity_nbr
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)





#Создание заказов
@login_required(login_url='/auth/login/')
def order_add(request):

    product_in_basket = ProductsInBasket.objects.filter(user=request.user, is_active=True, order__isnull=True)
    form = UserForBasket(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            username = data["client_username"]
            total_price = data["total_price"]
            user = User.objects.get(username=username)
             
            order = Order.objects.create(user=user, status_id = 1, total_price=total_price)                                                                                                        
            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductsInBasket.objects.get(id=product_in_basket_id)
                    
                    product_in_basket.quantity_nbr = value
                    product_in_basket.order = order
                    product_in_basket.is_active = False
                    product_in_basket.save(force_update=True)
                    
                    ProductsInOrder.objects.create(product=product_in_basket.product,
                                                   quantity_nbr = product_in_basket.quantity_nbr, 
                                                   price_per_item = product_in_basket.price_per_item, 
                                                   total_price=product_in_basket.total_price, 
                                                   order = order)
#            return redirect('pay:pay')
        else:
            print("no")

                    
    return render(request, 'basket/basket.html', locals())