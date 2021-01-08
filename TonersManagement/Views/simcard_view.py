from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib import messages
from ..models import *
from ..forms import *

from .authentication_view import *
from django.contrib.auth.decorators import login_required 
from django.shortcuts import HttpResponse
from django.http import HttpResponse
import datetime

@login_required(login_url='login')
def simcards(request):
    simcard_list = Simcard.objects.all()
    
    page = request.GET.get('page',1)
    paginator = Paginator(simcard_list,6)
    try: 
        simcardcollection = paginator.page(page)
    except PageNotAnInteger: 
        simcardcollection = paginator.page(1)
    except EmptyPage : 
        simcardcollection = paginator.page(paginator.num_pages)

    form = SimcardForm() 
    if request.method == 'POST':     
        form = SimcardForm(request.POST)
     
        if form.is_valid() : 
            form.save()
            messages.success(request,"Success",extra_tags="success")
            return redirect('/simcards')          
        else :
            messages.error(request,"Simcard already exist", extra_tags="danger")
            return Response("Toner already exist")
   
    return render(request, 'TonersManagement/pages/simcards.html',{'model':"Simcard",'data': simcardcollection,'form': form,  'headers':["Number","Seriel Number","Customer","Operator","Offer","Starting date","Ending date","Update","Delete"]} )
    

@login_required(login_url='login')
def djezzy(request):
    simcard_list = Simcard.objects.filter(operator="DJEZZY")
    
    page = request.GET.get('page',1)
    paginator = Paginator(simcard_list,6)
    try: 
        simcardcollection = paginator.page(page)
    except PageNotAnInteger: 
        simcardcollection = paginator.page(1)
    except EmptyPage : 
        simcardcollection = paginator.page(paginator.num_pages)

    form = SimcardForm() 
    if request.method == 'POST':     
        form = SimcardForm(request.POST)
     
        if form.is_valid() : 
            form.save()
            messages.success(request,"Success",extra_tags="success")
            return redirect('/simcards')          
        else :
            messages.error(request,"Simcard already exist", extra_tags="danger")
            return Response("Toner already exist")
   
    return render(request, 'TonersManagement/pages/simcards.html',{'model':"Simcard",'data': simcardcollection,'form': form,  'headers':["Number","Seriel Number","Customer","Operator","Offer","Starting date","Ending date","Update","Delete"]} )
    
@login_required(login_url='login')
def ooredoo(request):
    simcard_list = Simcard.objects.filter(operator="OOREDOO")
    
    page = request.GET.get('page',1)
    paginator = Paginator(simcard_list,6)
    try: 
        simcardcollection = paginator.page(page)
    except PageNotAnInteger: 
        simcardcollection = paginator.page(1)
    except EmptyPage : 
        simcardcollection = paginator.page(paginator.num_pages)

    form = SimcardForm() 
    if request.method == 'POST':     
        form = SimcardForm(request.POST)
     
        if form.is_valid() : 
            form.save()
            messages.success(request,"Success",extra_tags="success")
            return redirect('/simcards')          
        else :
            messages.error(request,"Simcard already exist", extra_tags="danger")
            return Response("Toner already exist")
   
    return render(request, 'TonersManagement/pages/simcards.html',{'model':"Simcard",'data': simcardcollection,'form': form,  'headers':["Number","Seriel Number","Customer","Operator","Offer","Starting date","Ending date","Update","Delete"]} )
    
@login_required(login_url='login')
def mobilis(request):
    simcard_list = Simcard.objects.filter(operator="MOBILIS")
    
    page = request.GET.get('page',1)
    paginator = Paginator(simcard_list,6)
    try: 
        simcardcollection = paginator.page(page)
    except PageNotAnInteger: 
        simcardcollection = paginator.page(1)
    except EmptyPage : 
        simcardcollection = paginator.page(paginator.num_pages)

    form = SimcardForm() 
    if request.method == 'POST':     
        form = SimcardForm(request.POST)
     
        if form.is_valid() : 
            form.save()
            messages.success(request,"Success",extra_tags="success")
            return redirect('/simcards')          
        else :
            messages.error(request,"Simcard already exist", extra_tags="danger")
            return Response("Toner already exist")
   
    return render(request, 'TonersManagement/pages/simcards.html',{'model':"Simcard",'data': simcardcollection,'form': form,  'headers':["Number","Seriel Number","Customer","Operator","Offer","Starting date","Ending date","Update","Delete"]} )
    

@login_required(login_url='login')
def update_simcard(request, pk): 
    item = Simcard.objects.get(id=pk)   
    form = SimcardForm(instance=item)
    if request.method == 'POST' :
        form = SimcardForm(request.POST,instance=item)
        if form.is_valid(): 
            form.save()  
            messages.success(request,"Successfully updated. ",extra_tags="success")
            return redirect('/simcards')

    return render(request, 'TonersManagement/components/update_item.html',{'data':item ,'form': form,'title':"UPDATE SIMCARD" ,'redirect_url':"simcards"})


@login_required(login_url='login')
def delete_simcard(request,pk):
    object = Simcard.objects.get(id=pk)
    if request.method == "POST": 
        object.delete()
        messages.success(request,"Successfully deleted. ",extra_tags="success")
        return redirect('/simcards')
    return render(request, 'TonersManagement/components/delete_item.html',{'data':object,'title':"DELETE SIMCARD",'info':object.__str__,'delete_url':"simcards",'delete_tamplate':"delete_simcard"})
    
from Toners.utils import render_to_pdf 

from django_xhtml2pdf.utils import pdf_decorator

@pdf_decorator(pdfname='release_voucher.pdf')
def decharge_view(request, pk):
    item = ReleaseVoucher.objects.get(id=pk)
    consumption_list = Consumption.objects.filter(release_voucher_id=pk)
    context = {
        'release_voucher': item,
        'consumption_list' : consumption_list,
        'date': datetime.date.today(),
        'count' : consumption_list.count(),
    }

    resp = HttpResponse(content_type='application/pdf')
    return render(request, 'TonersManagement/pdf/discharge.html', context)