from django.shortcuts import redirect, render
from .models import Product
from django.urls import reverse
# Create your views here.


def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'product.html',{'product':product})



def like_or_unlike(request,id):
    product = Product.objects.get(id=id)

    if request.user in product.like.all():
        product.like.remove(request.user)
    
    else:
        product.like.add(request.user)
    
    return redirect(reverse('detail',kwargs={'id':product.id}))



def user_favourites(request):
    user_favourites = Product.objects.filter(like=request.user)
    return render(request,'user_favourite.html',{'user_favourites':user_favourites})