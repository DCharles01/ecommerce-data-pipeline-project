"""
URL configuration for ecommerceapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.conf.urls import url
# import sys
# sys.path.append('..')
from .views import product_api
from .views import product_list

urlpatterns = [
    path("admin/", admin.site.urls),
    # add product list html
    # path(r'products/', product_list, name='product_list'),
    path('api/products/', product_api, name='product_api'),
    path('home/', product_list, name='product_list')
    #url(r'^/products/', product_list)

]

# from .views import get_products

# urlpatterns = [
#     path('api/products/', get_products, name='get_products'),
# ]
