from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.contrib import messages
from ..models import *
from ..forms import TonerForm
from ..filters import TonerFiler
from .authentication_view import *
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required
 



def update_toner(request, pk): 
    item = Toner.objects.get(id=pk)   
    form = TonerForm(instance=item)
    if request.method == 'POST' :
        form = TonerForm(request.POST,instance=item)
        if form.is_valid(): 
            form.save()  
            messages.success(request,"Successfully updated. ",extra_tags="success")
            return redirect('/toners')

    return render(request, 'TonersManagement/components/update_item.html',{'data':item ,'form': form,'title':"UPDATE TONER" ,'redirect_url':"toners"})



def delete_toner(request,pk):
    object = Toner.objects.get(id=pk)
    if request.method == "POST": 
        object.delete()
        messages.success(request,"Successfully deleted. ",extra_tags="success")
        return redirect('/toners')
    return render(request, 'TonersManagement/components/delete_item.html',{'data':object,'title':"DELETE TONER",'info':object.__str__,'delete_url':"toners",'delete_tamplate':"delete_toner"})
    