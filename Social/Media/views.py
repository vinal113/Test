from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status

from .models import Profile, PostsModel
from .serializers import Profile_serializer, Post_serializer

# Profile view
class Home_PageView(APIView):
    """
    Retrieve, update, delete
    """
    def get(self, request, pk):
        try:
            model = Profile.objects.get(id=pk)
            serializer = Profile_serializer(model)
            model_posts = PostsModel.objects.filter(profile=model)
            post_Serializer = Post_serializer(model_posts, many=True)
            return Response({"Profile_data":serializer.data, "Posts":post_Serializer.data}, status=status.HTTP_200_OK)
        except Exception as a:
            return Response({"erroe": str(a)}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        try:
            feed = Profile.objects.get(id=pk)
            serializer = Profile_serializer(feed, data=request.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            model_object = Profile.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        model_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetProfile(APIView):
    """
    Create
    """
    def post(self, request):
        serializer = Profile_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class PostView(APIView):
    """
    Create
    """
    def get(self, request, pk):
        try:
            posts = PostsModel.objects.filter(id=pk).first
            serializer = Post_serializer(data=posts)
            return Response(serializer.data) 
        except Exception as error:
            return Response({"error":error}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        serializer = Post_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# Posts Create, retrive, Update, archive

# Home page : our services
# Second page my profile
# Second phase : multiusers can upload their prompts