from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookmarkViewSet

router = DefaultRouter()

router.register(
    r'bookmarks',
    BookmarkViewSet,
    basename='bookmark'
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token),
]