from rest_framework import serializers
from demo.models import *
class taskserializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(taskserializer, self).__init__(many=many, *args, **kwargs)
    class Meta:
        model=task
        fields='__all__'
class titleserializer(serializers.ModelSerializer):
    class Meta:
        model=task
        fields=['title','id']