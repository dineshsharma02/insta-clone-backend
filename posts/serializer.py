
from rest_framework import serializers
from .models import Post_Item, Post_like, Post_Comment
from django.contrib.auth.models import User
# from django.http.request import build


################# SERIALIZER FOR POSTING AN IMAGE #######################


class PostSerializerImageField(serializers.ModelSerializer):
    # def get_user_id(self,obj):
    #     self.context.get('user_id')
    # user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    # user_id = serializers.ReadOnlyField()
    image = serializers.ImageField(required=True)
    total_likes = serializers.ReadOnlyField()
    total_comments = serializers.ReadOnlyField()
    class Meta:
        model = Post_Item
        fields = "__all__"

    def get_username(self,obj):
        return str(obj.user_id)
    
    



    # def create(self, validated_data):
    #     user_id = self.get_user_id(self,validated_data)
    #     return Posts(user_id,**validated_data)



#################### SERIALIZER FOR LIKES #########################

class Postlike_Serializer(serializers.ModelSerializer):
    
    # user_id = serializers.ReadOnlyField()
    # post_id = serializers.CharField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post_like
        fields = ['user_id','post_id','username']
        # read_only_fields = ['user_id']
    def get_username(self,obj):
        return str(obj.user_id)



############# SERIALIZER FOR POST COMMENT #####################

class Post_Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Comment
        fields = "__all__"
        # read_only_fields = ['user_id']


class User_Post_Details_Serializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    
    image = serializers.SerializerMethodField('get_image_url')
    # first_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post_Item
        fields = "__all__"
        # read_only_fields = ["__all__"]    

    def get_username(self,obj):
        return str(obj.user_id)

    def get_image_url(self,obj):
        request = self.context.get('request')
        photo_url = obj.image.url
        return request.build_absolute_uri(photo_url)

    
        # return str(User.objects.get(id=obj.user_id).first_name)