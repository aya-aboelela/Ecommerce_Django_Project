from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<int:categoryid>/',views.category,name="Category"),
    path('product/<int:productid>/',views.product,name="Product"),
    path('newproduct/',views.newproduct,name="newproduct"),


    path('addcart/<int:proid>/', views.addcart, name='addcarts'),
    path('cartitem/', views.cartitem, name='cartitem'),
    path('deleteitem/<int:proid>/', views.deleteitem, name='delete'),
] 