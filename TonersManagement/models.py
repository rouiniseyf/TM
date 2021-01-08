from django.db import models
from django.core.exceptions import ObjectDoesNotExist  
from datetime import date
# Create your models here.

def increment_invoice_number():
    all_releases = ReleaseVoucher.objects.all().order_by('id')
    last_invoice = ReleaseVoucher.objects.all().order_by('id').last()
    if not last_invoice or (all_releases[len(all_releases)-1].release_date.year != date.today().year):
         return 'BST0001'
    invoice_no = last_invoice.release_number
    invoice_int = int(invoice_no.split('BST')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = 'BST' + format(new_invoice_int, '04d')  
    return new_invoice_no

class Toner(models.Model): 
    description = models.CharField(max_length=80) 
    COLORS = (
        ('BK','BLACK'),
        ('MG','MAGENTA'), 
        ('CN','CYAN'), 
        ('YW','YELLOW')
    )
    color = models.CharField(max_length=10, null= True, choices=COLORS)
    TONERS_TYPES = (
        ('COMPATIBLE','COMPATIBLE'),
        ('ORIGINAL','ORIGINAL') )
    toners_type = models.CharField(max_length=100, null= True, choices=TONERS_TYPES)
    Quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.description +" "+ self.toners_type +" "+ self.color
    class Meta:
        unique_together = ["description", "color", "toners_type"]
        ordering = ["-id"]

class Direction(models.Model):
    description = models.CharField(max_length=250) 
    def __str__(self):
        return self.description 

class Customer(models.Model): 
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200,verbose_name='Full Name')
    def __str__(self):
        return self.full_name

class ReleaseVoucher(models.Model):
    release_number = models.CharField(max_length=9,default=increment_invoice_number)
    release_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    validated = models.BooleanField(default=False) 
    def __str__(self):
        return self.release_number
    
class Consumption(models.Model):
    release_voucher = models.ForeignKey(ReleaseVoucher, on_delete=models.CASCADE) 
    toner = models.ForeignKey(Toner, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0) 
    date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = ["release_voucher", "toner"]
        ordering = ["-id"]
    def __str__(self):
        return  self.toner.description +" "+ str(self.date)
    
class Offer(models.Model):
    descrption = models.CharField(max_length=150)
    price = models.FloatField(default=0)
    TYPES = (
        ('MOBILE', 'MOBILE'),
        ('DATA','DATA')
    )
    sim_type = models.CharField(max_length=10,null = False , choices=TYPES) 
    def __str__(self):
        return  self.descrption 
     
class Simcard(models.Model):
    number = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    starting_date = models.DateField(auto_now=False)
    OPERATORS = (
        ('DJEZZY', 'DJEZZY'),
        ('MOBILIS', 'MIBILIS'),
        ('OOREDOO','OOREDOO')
    )
    operator = models.CharField(max_length=10, null=False, choices=OPERATORS)
    ending_date = models.DateField(auto_now=False, null = True)
    seriel_number = models.CharField(max_length=50)

    def __str__(self):
        return  str(self.number) 
     
class Hardware(models.Model):
    seriel_number = models.CharField(max_length=30)
    inventory_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    DEVICES = (
        ('LAPTOP', 'LAPTOP'),
        ('PC FIX', 'PC FIX'),
        ('ECRAN', 'ECRAN'),
        ('IMPRIMANTE','IMPRIMANTE')
    )
    device = models.CharField(max_length=20, choices=DEVICES)
    description = models.CharField(max_length=30, blank=True)
    discharge_number = models.CharField(max_length=30, blank=True)
    supplier =   models.CharField(max_length=100, blank=True)
    bill_number = models.CharField(max_length=30, blank=True)
    release_voucher = models.CharField(max_length=30, blank=True)
    buying_date = models.DateField(auto_now=False, null = True)
    
    def __str__(self):
        return str(self.device + "  " + self.description)