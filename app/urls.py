"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('about',views.about,name='about'),
    path('aevent',views.anirudhevent,name='aevents'),
    path('contact',views.contact,name='contact'),
    path('event',views.event,name='eventspage'),
    path('general',views.general,name='gepage'),
    path('gold',views.gold,name='glpage'),
    path('join',views.join,name='join'),
    path('platinum',views.platinum,name='plpage'),
    #path('login',TemplateView.as_view(template_name='account/login.html') ,name='login'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('',views.home,name='home'),
    path('password',views.PasswordsChangeView.as_view(template_name='passwordchange.html'),name='passwordchange'),
    path('orders',views.orders,name='myorders'),
    path('Update Profile',views.editprofile.as_view(),name='updateprofile'),
    path('cart',views.cart,name='cart'),
    path('delete/<int:id>',views.deleteplatinumcartdata,name='delete'),
    path('delete/<int:id>',views.deletegoldcartdata,name='delete'),
    path('deletegold/<int:id>',views.deletegoldcartdata,name='delete'),
    path('deletegeneral/<int:id>',views.deletegeneralcartdata,name='delete'),
    path('platinumpaid/<int:id>',views.platinumpaid,name='paid'),
    path('goldpaid/<int:id>',views.goldpaid,name='paid'),
    path('generalpaid/<int:id>',views.generalpaid,name='paid'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)