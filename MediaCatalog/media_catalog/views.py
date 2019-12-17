from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


from . models import Media, Category, Provider, Creator
from . serializers import (
						MediaSerializer, 
						CategorySerializer, 
						CreatorSerializer, 
						ProviderSerializer)


class MediaViewSet(viewsets.ModelViewSet):
	queryset = Media.objects.all().order_by('-date_published')
	serializer_class = MediaSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['title', 'originating_country', 'genre', 'artist', 'publisher']

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['name', 'description']

class CreatorViewSet(viewsets.ModelViewSet):
	queryset = Creator.objects.all()
	serializer_class = CreatorSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['name', 'date_of_birth']

class ProviderViewSet(viewsets.ModelViewSet):
	queryset = Provider.objects.all()
	serializer_class = ProviderSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['name', 'provider_rank']

