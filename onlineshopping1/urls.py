"""onlineshopping1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from controller import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openadminlogin', openadminlogin),
    path('admin', openadminlogin),
    path('checkadminlogin', checkadminlogin),
    path('admindashboard', admindashboard),
    path('openadminchangepass', openadminchangepass),
    path('changeadminpassword', changeadminpassword),
    path('adminlogout', adminlogout),
    path('openaddproducts', openaddproducts),
    path('addproduct', addproduct),
    path('viewproducts', viewproducts),
    path('openviewproducts', openviewproducts),
    path('deleteproduct', deleteproduct),
    path('gotoeditproductpage', gotoeditproductpage),
    path('editproduct', editproduct),
    path('manageproductphotos', manageproductphotos),
    path('insertphoto', insertphoto),
    path('deleteproductphoto', deleteproductphoto),
    path('openuserdashboard', openuserdashboard),
    path('insertcart', insertcart),
    path('viewfilteredproducts', viewfilteredproducts),
    path('addtocart', addtocart),
    path('viewcart', viewcart),
    path('productdetailpage', productdetailpage),
    path('', website),
    path('about', about),
    path('contact', contact),
    path('vieworders', vieworders),
    path('deleteitemfromcart', deleteitemfromcart),
    path('fetchorders', fetchorders),
    path('orderdetail', orderdetail),
    path('getallproducts', getallproducts),
    path('gotoproductdetailfromhome', gotoproductdetailfromhome)
]
