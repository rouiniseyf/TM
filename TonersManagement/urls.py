from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Home),
    
    path('release_voucher/',views.ReleaseVoucherPage, name='release_voucher'),
    path('delete_toner/<str:pk>/', views.delete_toner, name='delete_toner'),
    path('update_toner/<str:pk>/', views.update_toner, name='update_toner'),
    path('register/',views.register, name='register'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('customers/',views.Customers, name='customers'),
    path('update_customer/<str:pk>/',views.update_customer, name='update_customer'),
    path('delete_customer/<str:pk>/',views.delete_customer, name='delete_customer'),
    path('update_relaese_voucher/<str:pk>/',views.update_release_voucher, name='update_release_voucher'),
    path('delete_release_voucher/<str:pk>/',views.delete_release_voucher, name='delete_release_voucher'),
    path('release_voucher_details/<str:pk>/',views.release_details, name='release_voucher_details'),
    path('pdf/<str:pk>/', views.report_view, name='report'),
    path('pdf/<str:pk>/', views.report_view, name='report'),
    path('validation/<str:pk>/', views.validate, name='validate'),
    path('update_consumption/<str:pk>/',views.update_consumption, name='update_consumption'),
    path('delete_consumption/<str:pk>/', views.delete_consumption, name='delete_consumpion'),
    path('simcards/',views.simcards, name='simcards'),
    path('delete_simcard/<str:pk>/', views.delete_simcard, name='delete_simcard'),
    path('update_simcard/<str:pk>/', views.update_simcard, name='update_simcard'),
    path('offers/',views.offers, name='offers'),
    path('delete_offer/<str:pk>/', views.delete_offer, name='delete_offer'),
    path('update_offer/<str:pk>/', views.update_offer, name='update_offer'),
    path('djezzy/',views.djezzy, name='djezzy'),
    path('ooredoo/',views.ooredoo, name='ooredoo'),
    path('mobilis/',views.mobilis, name='mobilis'),
    path('print_reports/',views.consumption_report, name='print_report'),
    path('reports/',views.report_consumption_all_range, name='consumption_all_range'),
    path('hardware/',views.hardware, name='hardware'),
    path('delete_hardware/<str:pk>/', views.delete_hardware, name='delete_hardware'),
    path('update_hardware/<str:pk>/', views.update_hardware, name='update_hardware'),
      
]
