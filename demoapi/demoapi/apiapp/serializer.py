
from rest_framework import serializers
from apiapp.models import desc

class dataserializer(serializers.Serializer):
    id  = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    
    def create(self,data):
        return desc.objects.create(**data)
    
    def update(self,instance,data):
        instance.title = data.get('title',instance.title)
        instance.description = data.get('description',instance.description)
        instance.save()
        return instance
        