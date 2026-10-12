from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Language
from .serializers import LanguageSerializer

# Create your views here.


class LanguageListAPIView(ListAPIView):
    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer
    pagination_class = PageNumberPagination


class LanguageDetailAPIView(RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'iso'
    lookup_url_kwarg = 'iso'
