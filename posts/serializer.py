
from nbformat import read
from rest_framework import serializers
from .models import Posts

class PostSerializerImageField(serializers.ModelSerializer):
    def get_user_id(self,obj):
        self.context.get('user_id')
    # user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # user_id = serializers.ReadOnlyField()
    
    image = serializers.ImageField(required=True)
    total_likes = serializers.ReadOnlyField()
    total_comments = serializers.ReadOnlyField()
    class Meta:
        model = Posts
        fields = "__all__"
    
    # def create(self, validated_data):
    #     user_id = self.get_user_id(self,validated_data)
    #     return Posts(user_id,**validated_data)

    

        # edi