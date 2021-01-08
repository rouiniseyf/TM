from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib import messages
from ..models import ReleaseVoucher , Consumption , Customer , Toner 
from ..forms import ReleaseVoucherForm, ConsumptionForm
from ..filters import TonerFiler
from .authentication_view import *
from django.contrib.auth.decorators import login_required 
from django.shortcuts import HttpResponse
from django.http import HttpResponse
import datetime
from django.core.mail import send_mail


context = {}
filtered_list = []
customer_name = "/"
direction_name = "/"

@login_required(login_url='login')    
def report_consumption_all_range(request):
    date_from = request.POST.get('date_from')
    date_to = request.POST.get('date_to')
    # Get consumption by direction or 
    global filtered_list
    global customer_name
    global direction_name
    if request.method == 'POST' and 'submit_consumption_ny_direction' in request.POST:
        direction_name = request.POST.get('direction')
        if (direction_name == 'ALL'):
            customer_name = "/"
            filtered_list = get_consumption(date_from, date_to)   
        else:
            customer_name = "/"
            direction = Direction.objects.get(description=direction_name)
            filtered_list = get_consumption_direction(date_from, date_to, direction.id)
    # Get consumption by customer
    if request.method == 'POST' and 'submit_consumption_by_customer' in request.POST:
         direction_name = "/"
         customer_name = request.POST.get('customer')
         customer = Customer.objects.get(full_name=customer_name)
         filtered_list = get_consumption_customer(date_from, date_to,customer.id)
    # Context    
    global context  
    context = {
        'consumption_list' : filtered_list ,
        'headers': ['Toner', 'Release Voucher', 'Customer', 'Quantity', 'Date'],
        'today': datetime.date.today(),
        'directions': Direction.objects.all(),
        'customers': Customer.objects.all(),
        'from': "/" if date_from == None else  date_from ,
        'to': "/" if date_to == None else date_to,
        'selected_custoemr':  customer_name,
        'selected_direction':  direction_name,
        }
    if request.method == 'POST' and 'print' in request.POST:
        print('ok')
        return redirect('print_report')
        
    return render(request,'TonersManagement/pages/consumption_report.html', context)



def get_consumption(date_from, date_to):

    filtered_list = Consumption.objects.filter(date__range = (date_from, date_to))
    return filtered_list
    
def get_consumption_direction(date_from, date_to , direction):

    filtered_list = Consumption.objects.filter(date__range = (date_from, date_to) , release_voucher__customer__direction_id = direction)
    return filtered_list
    
def get_consumption_customer(date_from, date_to, customer):

    filtered_list = Consumption.objects.filter(date__range = (date_from, date_to) , release_voucher__customer__id = customer)
    return filtered_list
    

from Toners.utils import render_to_pdf 

from django_xhtml2pdf.utils import pdf_decorator

@pdf_decorator(pdfname='Consumption_report.pdf')
def consumption_report(request):
    global context 
    print(context)
    resp = HttpResponse(content_type='application/pdf')
    return render(request, 'TonersManagement/pdf/consumption_report.html', context)

