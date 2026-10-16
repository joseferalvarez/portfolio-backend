from django.urls import path

from .views import SocialMediaDetailApiView, SocialMediaListApiView

urlpatterns = [
    path('', SocialMediaListApiView.as_view(), name='social-media-list'),
    path(
        '<str:slug>',
        SocialMediaDetailApiView.as_view(),
        name='social-media-detail',
    ),
]
