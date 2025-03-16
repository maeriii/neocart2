
from django.contrib import admin
from django.urls import path
from NeoApp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('blogs/',views.blog_details,name='blogs'),
    path('starter/',views.starter,name='starter'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('transaction/', views.transactions_list, name='transaction'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
