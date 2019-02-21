from rest_framework import serializers
from customers.models import customers
from movies.models import mmovies

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = mmovies
        fields= '__all__'
        #fields= 'mname','genre','year','description','price','fname'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model=customers
        fields= '__all__'
        #fields='fname','lname','birthdate','pnumber','address'