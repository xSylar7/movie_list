from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import permissions
from movies import serializers
from .models import Movie
# Create your views here.


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     if user


class UserCreateView (generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer


class UserLoginView(views.APIView):
    serialzer_class = serializers.UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = serializers.UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
