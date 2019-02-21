import django_filters
from .models import customers


class custfilter(django_filters.FilterSet):

	class Meta:
		model = customers
		fields = ('fname', 'lname', 'birthdate','pnumber','address')