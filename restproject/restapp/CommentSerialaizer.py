
from rest_framework import serializers
from .models import Comment
class CommentSerialaizerIn(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['age','name','angl']


class CommentSerialaizerOut(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','age','name','angl','status']

class ItemSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=50)
        color = serializers.CharField(max_length=50)
        weight = serializers.IntegerField()
        price = serializers.FloatField()
        discount = serializers.BooleanField()
