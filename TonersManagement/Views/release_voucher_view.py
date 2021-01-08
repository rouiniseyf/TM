from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib import messages
from ..models import ReleaseVoucher, Consumption , Toner
from ..forms import ReleaseVoucherForm, ConsumptionForm
from ..filters import TonerFiler
from .authentication_view import *
from django.contrib.auth.decorators import login_required 
from django.shortcuts import HttpResponse
from django.http import HttpResponse
import datetime
from django.core.mail import send_mail

@login_required(login_url='login')
def ReleaseVoucherPage(request):
    releases_list = ReleaseVoucher.objects.all()
    
    page = request.GET.get('page',1)
    paginator = Paginator(releases_list,6)
    try: 
        releases = paginator.page(page)
    except PageNotAnInteger: 
        releases = paginator.page(1)
    except EmptyPage : 
        releases = paginator.page(paginator.num_pages)

    form = ReleaseVoucherForm() 
    if request.method == 'POST' : 
        form = ReleaseVoucherForm(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request, "Success", extra_tags="success")           
            return redirect('/release_voucher')
            
        else :
            messages.error(request,"Realse already exist", extra_tags="danger")
            return redirect('/release_voucher')
    return render(request, 'TonersManagement/pages/releases.html',{'model':"Release",'data': releases,'form': ReleaseVoucherForm,  'headers':["Release Number","Customer","Direction","Release Date","Update","Delete"]} )


    
def update_release_voucher(request, pk): 
    item = ReleaseVoucher.objects.get(id=pk)   
    form = ReleaseVoucherForm(instance=item)
    if request.method == 'POST' :
        form = ReleaseVoucherForm(request.POST,instance=item)
        if form.is_valid(): 
            form.save()  
            messages.success(request,"Successfully updated. ",extra_tags="success")
            return redirect('/release_voucher')

    return render(request, 'TonersManagement/components/update_item.html',{'data':item ,'form': form,'title':"UPDATE RELEASE VOUCHER" ,'redirect_url':"release_voucher"})



def delete_release_voucher(request,pk):
    object = ReleaseVoucher.objects.get(id=pk)

    if request.method == "POST": 
        object.delete()
        messages.success(request,"Successfully deleted. ",extra_tags="success")
        return redirect('/release_voucher')
    return render(request, 'TonersManagement/components/delete_item.html',{'data':object,'title':"DELETE RELEASE VOUCHER",'info':object.__str__,'delete_url':"release_voucher",'delete_tamplate':"delete_release_voucher"})
    
def release_details(request,pk):
    item = ReleaseVoucher.objects.get(id=pk)
    consumption_list = Consumption.objects.filter(release_voucher_id=item.id)
    form = ConsumptionForm(initial={'release_voucher': item}) 
    if request.method == 'POST':
        form = ConsumptionForm(request.POST)
        selected_toner = Toner.objects.get(id = request.POST['toner'])
        if int(request.POST['quantity']) > selected_toner.Quantity : 
            messages.error(request, "Not enough quantity of" + selected_toner.description , extra_tags="danger")
        else: 
            if form.is_valid():
                new_quantity = selected_toner.Quantity - int(request.POST['quantity'])
                Toner.objects.filter(pk=selected_toner.pk).update(Quantity=new_quantity)
                form.save()
                messages.success(request,"Success",extra_tags="success")
            else :
                messages.error(request,"Realse already exist", extra_tags="danger")
                return redirect('/toners')
    return render(request,'TonersManagement/pages/release_details.html',{'customers':Toner.objects.all() ,'data': item,'form':form,'consumption_list':consumption_list,'headers':["Toner","Color","Type","Quantity","Date","Update","Delete"]})


def update_consumption(request, pk): 
    item = Consumption.objects.get(id=pk)   
    form = ConsumptionForm(instance=item)
    if request.method == 'POST' :
        form = ConsumptionForm(request.POST,instance=item)
        if form.is_valid(): 
            form.save()  
            messages.success(request,"Successfully updated. ",extra_tags="success")
            return redirect('/release_voucher')

    return render(request, 'TonersManagement/components/update_item.html',{'data':item ,'form': form,'title':"UPDATE LINE" ,'redirect_url':"release_voucher"})



def delete_consumption(request,pk):
    object = Consumption.objects.get(id=pk)
  
    #current_quantity = Toner.objects.get(id = request.POST['toner'])
    if request.method == "POST": 
        object.delete()
        current_quantity = object.toner.Quantity
        new_quantity = current_quantity + object.quantity 
        Toner.objects.filter(pk=object.toner.id).update(Quantity=new_quantity)
        messages.success(request,"Successfully deleted. ",extra_tags="success")
        return redirect('/release_voucher')
    return render(request, 'TonersManagement/components/delete_item.html',{'data':object,'title':"DELETE LINE",'info':object.__str__,'delete_url':"release_voucher",'delete_tamplate':"delete_consumpion"})
    


from Toners.utils import render_to_pdf 

from django_xhtml2pdf.utils import pdf_decorator

@pdf_decorator(pdfname='release_voucher.pdf')
def report_view(request, pk):
    item = ReleaseVoucher.objects.get(id=pk)
    consumption_list = Consumption.objects.filter(release_voucher_id=pk)
    context = {
        'release_voucher': item,
        'consumption_list' : consumption_list,
        'date': datetime.date.today(),
        'count' : consumption_list.count(),
    }

    resp = HttpResponse(content_type='application/pdf')
    return render(request, 'TonersManagement/pdf/release_voucher_pdf.html', context)


def validate(request, pk):
    item = ReleaseVoucher.objects.get(id=pk)
    consumption_list = Consumption.objects.filter(release_voucher_id=pk)
    message = ""
    for i in consumption_list:
        message += i.toner.description + " " + i.toner.color +  " |"
    send_mail(
                'Sortie Toner',
                message,
                'from@example.com',
                ['rouiniseyf.al@gmail.com'],
                fail_silently=False,
            )
    return 'ok'


def reports(request):
    
    return render(request, 'TonersManagement/pages/reports.html')