import django_filters  
from django_filters import DateFilter, CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    startdate = DateFilter(field_name='date_created',lookup_expr='gte')
    enddate = DateFilter(field_name='date_created',lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']