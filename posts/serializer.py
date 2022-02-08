
from nbformat import read
from rest_framework import serializers
from .models import Post_Item, Post_like


################# SERIALIZER FOR POSTING AN IMAGE #######################


class PostSerializerImageField(serializers.ModelSerializer):
    def get_user_id(self,obj):
        self.context.get('user_id')
    # user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # user_id = serializers.ReadOnlyField()
    
    image = serializers.ImageField(required=True)
    total_likes = serializers.ReadOnlyField()
    total_comments = serializers.ReadOnlyField()
    class Meta:
        model = Post_Item
        fields = "__all__"
    
    # def create(self, validated_data):
    #     user_id = self.get_user_id(self,validated_data)
    #     return Posts(user_id,**validated_data)



#################### SERIALIZER FOR LIKES #########################

class Postlike_Serializer(serializers.ModelSerializer):
    
    # user_id = serializers.ReadOnlyField()
    # post_id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Post_like
        fields = ['user_id','post_id']
        # read_only_fields = ['user_id']

