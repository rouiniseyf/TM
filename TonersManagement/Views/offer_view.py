from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib import messages
from ..models import *
from ..forms import ReleaseVoucherForm, ConsumptionForm , OfferForm

from .authentication_view import *
from django.contrib.auth.decorators import login_required 
from django.shortcuts import HttpResponse
from django.http import HttpResponse
import datetime

@login_required(login_url='login')
def offers(request):
    offers_list = Offer.objects.all()
    
    page = request.GET.get('page',1)
    paginator = Paginator(offers_list,6)
    try: 
        offers_page = paginator.page(page)
    except PageNotAnInteger: 
        offers_page = paginator.page(1)
    except EmptyPage : 
        offers_page = paginator.page(paginator.num_pages)

    form = OfferForm() 
    if request.method == 'POST':     
        form = OfferForm(request.POST)
     
        if form.is_valid() : 
            form.save()
            messages.success(request,"Success",extra_tags="success")
            return redirect('/offers')          
        else :
            messages.error(request,"offers already exist", extra_tags="danger")
            return Response("Offers already exist")
   
    return render(request, 'TonersManagement/pages/offers.html',{'model':"Offer",'data': offers_page,'form': OfferForm,  'headers':["Description","Price","Type","Update","Delete"]} )
    


def update_offer(request, pk): 
    item = Offer.objects.get(id=pk)   
    form = OfferForm(instance=item)
    if request.method == 'POST' :
        form = OfferForm(request.POST,instance=item)
        if form.is_valid(): 
            form.save()  
            messages.success(request,"Successfully updated. ",extra_tags="success")
            return redirect('/offers')

    return render(request, 'TonersManagement/components/update_item.html',{'data':item ,'form': form,'title':"UPDATE OFFER" ,'redirect_url':"offers"})



def delete_offer(request,pk):
    object = Offer.objects.get(id=pk)
    if request.method == "POST": 
        object.delete()
        messages.success(request,"Successfully deleted. ",extra_tags="success")
        return redirect('/offers')
    return render(request, 'TonersManagement/components/delete_item.html',{'data':object,'title':"DELETE OFFER",'info':object.__str__,'delete_url':"offers",'delete_tamplate':"delete_offer"})
    