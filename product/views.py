from django.shortcuts import redirect, render
from .models import Category, Product,order
from django.contrib.auth.decorators import login_required


def home(request):
    allcategories = Category.objects.all()
    allproducts = Product.objects.all()
    return render(request, 'home.html',{"allproducts":allproducts,"allcategories":allcategories})

def category(request,categoryid):
    allcategories = Category.objects.all()
    mycategory = Category.objects.get(id=categoryid)
    allproducts = Product.objects.all().filter(category_id = categoryid )
    return render(request,'category.html',{"allproducts":allproducts,"allcategories":allcategories,"mycategory":mycategory})

def product(request,productid):
    allcategories = Category.objects.all()
    myproduct = Product.objects.get(id=productid)
    return render(request,'product.html',{"allcategories":allcategories,"myproduct":myproduct})

def newproduct(request):
    allcategories = Category.objects.all()
    allproducts = Product.objects.all().order_by("-id")
    return render(request,'newproduct.html',{"allproducts":allproducts,"allcategories":allcategories})


@login_required(login_url='/login/')
def addcart(request,proid):
    quantity=int(order.objects.filter(productid=proid).count())
    if quantity >= 1:
        ca=order.objects.get(productid=proid)
        order.objects.filter(productid=proid).update(num=int(ca.num)+1)
    else:
        id = request.user.id
        carts=order(productid=proid,user_id=id,num=1)
        carts.save()
    return redirect("/cartitem/")

@login_required(login_url='/login/')
def deleteitem(request,proid):
    item=order.objects.get(id=proid)
    item.delete()
    return redirect("/cartitem/")

@login_required(login_url='/login/')
def cartitem(request):
    quantity = 0
    price =0
    allcategories = Category.objects.all()
    products = Product.objects.all()
    orderss = order.objects.filter(user_id=request.user.id)
    for v in orderss:
        quantity=quantity+int(v.num)
        for f in Product.objects.all():
            if v.productid ==f.id:
                price =price +(int(f.price)*int(v.num))
    return render(request, 'cartitem.html',{"products":products,'quantity':quantity,"price":price,"orders":orderss,"allcategories":allcategories})

        

    