import django_filters
from .models import * 
from django_filters import CharFilter 

class TonerFiler(django_filters.FilterSet):
    Toner = CharFilter(field_name='description',lookup_expr='icontains')
    class Meta: 
        model = Toner 
        fields = '__all__'

