from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib import messages
from ..models import Hardware
from ..forms import HardwareFrom
from .authentication_view import *
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required
 

@login_required(login_url='login')
def hardware(request):
    hardware_list = Hardware.objects.all()
    
    page = request.GET.get('page',1)
    paginator = Paginator(hardware_list,6)
    try: 
        hardware = paginator.page(page)
    except PageNotAnInteger: 
        hardware = paginator.page(1)
    except EmptyPage : 
        hardware = paginator.page(paginator.num_pages)

    form = HardwareFrom() 
    if request.method == 'POST':     
        form = HardwareFrom(request.POST)
     
        if form.is_valid() : 
            form.save()
            messages.success(request,"Success",extra_tags="success")
            return redirect('/hardware')          
        else :
            messages.error(request,"device already exist", extra_tags="danger")
            return Response("device already exist")
   
    return render(request, 'TonersManagement/pages/Hardware.html',{'model':"Hardware",'data': hardware,'form': HardwareFrom,  'headers':["Device","Description","Seriel","Inventory","Customer","Discharge","Supplier","Bill","Release Voucher","Date","Update","Delete"]} )
    

def update_hardware(request, pk): 
    item = Hardware.objects.get(id=pk)   
    form = HardwareFrom(instance=item)
    if request.method == 'POST' :
        form = HardwareFrom(request.POST,instance=item)
        if form.is_valid(): 
            form.save()  
            messages.success(request,"Successfully updated. ",extra_tags="success")
            return redirect('/hardware')

    return render(request, 'TonersManagement/components/update_item.html',{'data':item ,'form': form,'title':"UPDATE HARDWARE" ,'redirect_url':"hardware"})



def delete_hardware(request,pk):
    object = Hardware.objects.get(id=pk)
    if request.method == "POST": 
        object.delete()
        messages.success(request,"Successfully deleted. ",extra_tags="success")
        return redirect('/hardware')
    return render(request, 'TonersManagement/components/delete_item.html',{'data':object,'title':"DELETE HARDWARE",'info':object.__str__,'delete_url':"hardware",'delete_tamplate':"delete_hardware"})
    