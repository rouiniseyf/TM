from django.db import models
from django.core.exceptions import ObjectDoesNotExist  
# Create your models here.

def increment_invoice_number():
    try:
        last_invoice = ReleaseVoucher.objects.raw("SELECT max(release_number),id from TonersManagement_releasevoucher WHERE  strftime('%Y', release_date) = strftime('%Y', CURRENT_TIMESTAMP)")[0]
    except ReleaseVoucher.DoesNotExist:
        last_invoice = 'BST000001'
   # if not last_invoice:
     #    return 'BST000001'
    invoice_no = last_invoice.release_number
    invoice_int = int(invoice_no.split('BST')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = 'BST' + format(new_invoice_int, '06d')  
    return new_invoice_no

class Reference(models.Model): 
    reference = models.CharField(max_length=100)
    TONERS_TYPES = (
        ('Compatible','Compatible'),
        ('Original','Original') )
    _type = models.CharField(max_length=100, null= True, choices=TONERS_TYPES)
    def __str__(self):
        return self.reference + " " + self._type
    
class Toner(models.Model): 
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE)
    description = models.CharField(max_length=100) 
    Quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.reference.reference +" "+  self.description
    
class Direction(models.Model):
    description = models.CharField(max_length=250) 
    def __str__(self):
        return self.description

class Customer(models.Model): 
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    def __str__(self):
        return self.full_name

class ReleaseVoucher(models.Model):
    release_number = models.CharField(max_length=9,default=increment_invoice_number)
    release_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    def __str__(self):
        return self.release_number
    
class Consumption(models.Model):
    release_voucher = models.ForeignKey(ReleaseVoucher, on_delete=models.CASCADE) 
    toner = models.ForeignKey(Toner, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0) 
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.toner.reference.reference +" "+ self.toner.description +" "+ str(self.date)
    
