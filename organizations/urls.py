from rest_framework.routers import DefaultRouter
from .viewsets import OrganizationViewSet

app_name = "organizations"
router = DefaultRouter()

router.register(r"", OrganizationViewSet)

urlpatterns = router.urls