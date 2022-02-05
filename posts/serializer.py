
from nbformat import read
from rest_framework import serializers
from .models import Posts

class PostSerializerImageField(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # user_id = serializers.ReadOnlyField()
    image = serializers.ImageField(required=True)
    total_likes = serializers.ReadOnlyField()
    total_comments = serializers.ReadOnlyField()
    class Meta:
        model = Posts
        fields = '__all__'
        

        # edi