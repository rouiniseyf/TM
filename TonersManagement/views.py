from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib import messages
from .models import *
from .forms import TonerForm
from .filters import TonerFiler
from .Views.toner_view import *
from .Views.customers_view import *
from .Views.authentication_view import *
from .Views.release_voucher_view import *
from .Views.offer_view import *
from .Views.simcard_view import *
from django.db.models import Sum
from .Views.reports_view import *
from .Views.hardware_view import *
import datetime 
# Create your views here.
from django.contrib.auth.decorators import login_required 

@login_required(login_url='login')
def Home(request):
    low_on_stock = Toner.objects.filter(Quantity__lte=2, Quantity__gte=1)
    stock = Toner.objects.all()
    zero_in_stock = Toner.objects.filter(Quantity=0)
    count_low = low_on_stock.count()
    count_zero = zero_in_stock.count()
    count_stock = stock.count()
    djezzy_simcards = Simcard.objects.filter(operator="DJEZZY")
    djezzy_simcards_count = djezzy_simcards.count()
    ooredoo_simcards = Simcard.objects.filter(operator="OOREDOO")
    ooredoo_simcards_count = ooredoo_simcards.count()
    mobilis_simcards = Simcard.objects.filter(operator="MOBILIS")
    mobilis_simcards_count = mobilis_simcards.count()
    sum_djezzy = Simcard.objects.filter(operator="DJEZZY").aggregate(Sum('offer__price'))
    sum_ooredoo = Simcard.objects.filter(operator="OOREDOO").aggregate(Sum('offer__price'))
    sum_mobilis = Simcard.objects.filter(operator="MOBILIS").aggregate(Sum('offer__price'))
    total_sum = Simcard.objects.all().aggregate(Sum('offer__price'))
    context = {
        'count_low': count_low,
        'count_zero': count_zero,
        'count_stock': count_stock,
        'low_on_stock_list': low_on_stock,
        'zero_on_stock_list': zero_in_stock,
        'djezzy_simcards': djezzy_simcards,
        'djezzy_simcards_count': djezzy_simcards_count,
        'ooredoo_simcards': ooredoo_simcards,
        'ooredoo_simcards_count': ooredoo_simcards_count,
        'mobilis_simcards': mobilis_simcards,
        'mobilis_simcards_count': mobilis_simcards_count,
        'sum_djezzy': sum_djezzy['offer__price__sum'],
        'sum_ooredoo': sum_ooredoo['offer__price__sum'],
        'sum_mobilis': sum_mobilis['offer__price__sum'],
        'total_sum': total_sum['offer__price__sum'],
        }
    return render(request, 'TonersManagement/pages/home.html',context)

