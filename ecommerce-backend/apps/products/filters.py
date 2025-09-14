from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')
    created_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Product
        fields = ['name', 'category', 'price_min', 'price_max', 'created_at']