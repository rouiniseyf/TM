from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Home(request):
    return render(request, 'TonersManagement/pages/home.html')

def Toenrs(request):
    return render(request, 'TonersManagement/pages/toners.html')

def ReleaseVoucher(request): 
    return HttpResponse("Release Voucher")