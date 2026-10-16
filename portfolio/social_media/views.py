from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SocialMedia
from .serializers import SocialMediaListSerializer, SocialMediaSerializer

# Create your views here.


class SocialMediaListApiView(ListAPIView):
    queryset = SocialMedia.objects.all().order_by('name')
    serializer_class = SocialMediaListSerializer
    pagination_class = PageNumberPagination


class SocialMediaDetailApiView(APIView):
    def get(self, request, slug):
        slug_formatted = slug.replace('-', ' ')
        social_media = get_object_or_404(
            SocialMedia, name__iexact=slug_formatted
        )
        serializer = SocialMediaSerializer(social_media, many=False)
        return Response(serializer.data)
