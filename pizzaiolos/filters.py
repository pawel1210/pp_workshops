from .models import Pizzaiolo
import django_filters

class PizzaioloFilter(django_filters.FilterSet):
    first_name__icontains  = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains', label="First Name")
    last_name__icontains  = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains', label="Last Name")
    location__icontains  = django_filters.CharFilter(field_name='location', lookup_expr='icontains', label="Location")
    class Meta:
        model = Pizzaiolo
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'location': ['icontains'],
        }
