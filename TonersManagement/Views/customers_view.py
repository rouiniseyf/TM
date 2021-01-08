from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from ..models import *
from ..forms import TonerForm, CustomerForm
from ..filters import TonerFiler
from .authentication_view import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def Customers(request):
    customers_list = Customer.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(customers_list, 6)
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success", extra_tags="success")
            return redirect('/customers')
        else:
            messages.error(request,
                           "Customer already exist",
                           extra_tags="danger")
            return redirect('/customers')
    return render(
        request, 'TonersManagement/pages/customers.html', {
            'model': "Customer",
            'data': customers,
            'form': CustomerForm,
            'headers': ["Direction", "Full_name", "Update", "Delete"]
        })


def update_customer(request, pk):
    item = Customer.objects.get(id=pk)
    form = CustomerForm(instance=item)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Successfully updated. ",
                             extra_tags="success")
            return redirect('/customers')

    return render(
        request, 'TonersManagement/components/update_item.html', {
            'data': item,
            'form': form,
            'title': "UPDATE CUSTOMER",
            'redirect_url': "customers"
        })


def delete_customer(request, pk):
    object = Customer.objects.get(id=pk)
    if request.method == "POST":
        object.delete()
        messages.success(request,
                         "Successfully deleted. ",
                         extra_tags="success")
        return redirect('/customers')
    return render(
        request, 'TonersManagement/components/delete_item.html', {
            'data': object,
            'title': "DELETE CUSTOMER",
            'info': object.full_name,
            'delete_url': "customers",
            'delete_tamplate': "delete_customer"
        })
