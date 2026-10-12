from django.urls import path

from .views import LanguageDetailAPIView, LanguageListAPIView

urlpatterns = [
    path('', LanguageListAPIView.as_view(), name='language-list'),
    path('<str:iso>/', LanguageDetailAPIView.as_view(), name='language-detail'),
]
