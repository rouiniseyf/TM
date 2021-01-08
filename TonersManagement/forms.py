from django.forms import ModelForm 
from django import forms
from .models import Toner,Customer,ReleaseVoucher,Consumption ,Simcard, Offer, Hardware 
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
import datetime

class TonerForm(ModelForm):
    
    class Meta:
        model = Toner
        fields = '__all__'
        widgets = {
            'description' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'color' : forms.Select(attrs={'class':'form-control shadow-none'}),
            'toners_type' : forms.Select(attrs={'class':'form-control shadow-none'}),                      
            'Quantity' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
        }
        labels = {
            "toners_type": "Toenr Type",
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "are not unique.",
            }
        }

class CustomerForm(ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'direction' : forms.Select(attrs={'class':'form-control shadow-none'}),
            'full_name' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "are not unique.",
            }
        }

class CreateUserForm(UserCreationForm): 
    class Meta: 
        model = User
        fields= ['first_name','last_name','username','email', 'password1', 'password2']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'username' : forms.TextInput(attrs={'class':'form-control shadow-none'}),                    
            'email' : forms.EmailInput(attrs={'class':'form-control shadow-none'}),                    
            'password1' : forms.PasswordInput(attrs={'class':'form-control shadow-none'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control shadow-none'}),
        }

class ReleaseVoucherForm(ModelForm):
    
    class Meta:
        model = ReleaseVoucher
        fields = '__all__'

        widgets = {
            'release_number' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'release_date' : forms.DateInput(attrs={'type':'date' ,'class':'form-control shadow-none'}),
            'customer' : forms.Select(attrs={'class':'form-control shadow-none' }),
        }


class ConsumptionForm(ModelForm):
    
    class Meta:
        model = Consumption
        fields = '__all__'

        widgets = {
            'release_voucher' : forms.Select(attrs={'class':'form-control shadow-none','readonly':'readonly'}),
            'toner' : forms.Select(attrs={'class':'form-control shadow-none'}),
            'quantity' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
        }



class SimcardForm(ModelForm):
    
    class Meta:
        model = Simcard
        fields = '__all__'

        widgets = {
            'number' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'seriel_number' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'customer' : forms.Select(attrs={'class':'form-control shadow-none'}),
            'offer' : forms.Select(attrs={'class':'form-control shadow-none' }),
            'starting_date' :forms.DateInput(attrs={'type':'date' , 'value':datetime.date.today() , 'class':'form-control shadow-none' }),
            'ending_date' : forms.DateInput(attrs={'type':'date' , 'value':datetime.date.today() ,'class':'form-control shadow-none' }),
            'operator' : forms.Select(attrs={'class':'form-control shadow-none' }),
        }

class OfferForm(ModelForm):

    class Meta:
        model = Offer
        fields = '__all__'

        widgets = {
            'descrption' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'price' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'sim_type' : forms.Select(attrs={'class':'form-control shadow-none' }),         
        }
    
class HardwareFrom(ModelForm):
    
    class Meta:
        model = Hardware
        fields = '__all__'

        widgets = {
            'seriel_number' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'inventory_number' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'customer' : forms.Select(attrs={'class':'form-control shadow-none' }), 
            'device' : forms.Select(attrs={'class':'form-control shadow-none' }), 
            'description' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'discharge_number' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'supplier' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'bill_number' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'release_voucher' : forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'buying_date': forms.DateInput(attrs={'type':'date' , 'value':datetime.date.today() ,'class':'form-control shadow-none' }),
        }