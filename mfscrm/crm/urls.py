from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth.views import  LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

app_name = 'crm'
urlpatterns = [

    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('register/', views.register, name='register'),
    path('product_list', views.product_list, name='product_list'),
    path('product/create/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('customer/<int:pk>/summary/', views.summary, name='summary'),
    #path('customer/<int:pk>/summary_pdf/', views.GeneratePdf, name='summary_download'),
    path('customer/<int:pk>/detailed_summary/', views.download_summary_pdf, name='download_summary_pdf')




]
