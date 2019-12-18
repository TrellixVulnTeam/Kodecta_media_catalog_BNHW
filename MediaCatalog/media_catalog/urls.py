from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'api/media', views.MediaViewSet)
router.register(r'api/category', views.CategoryViewSet)
router.register(r'api/creator', views.CreatorViewSet)
router.register(r'api/provider', views.ProviderViewSet)
router.register(r'api/media-publish', views.MediaPublishViewSet)
router.register(r'api/user-media-publish', views.UserViewSet)

urlpatterns = router.urls