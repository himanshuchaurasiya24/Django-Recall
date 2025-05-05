import django_filters
from .models import Employee
from django.db.models.functions import Lower



class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='icontains')
    employee_name = django_filters.CharFilter(field_name='employee_name', lookup_expr='icontains')
    employee_id = django_filters.CharFilter(field_name='employee_id', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_id_min', label='From EMP ID')
    id_max = django_filters.CharFilter(method='filter_id_max', label='To EMP ID')

    class Meta:
        model = Employee
        fields = ['employee_name','employee_id','designation','id_min', 'id_max']

    def filter_id_min(self, queryset, name, value):
        return queryset.annotate(lower_id=Lower('employee_id')).filter(lower_id__gte=value.lower())

    def filter_id_max(self, queryset, name, value):
        return queryset.annotate(lower_id=Lower('employee_id')).filter(lower_id__lte=value.lower())
