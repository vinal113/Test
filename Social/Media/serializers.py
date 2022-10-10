from rest_framework import serializers
from .models import Profile, PostsModel

class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class Post_serializer(serializers.ModelSerializer):
    class Meta:
        model = PostsModel
        fields = "__all__"

