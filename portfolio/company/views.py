from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Company
from .serializers import CompanyListSerializer, CompanySerializer

# Create your views here.


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanyListSerializer
    pagination_class = PageNumberPagination


class CompanyDetailAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
