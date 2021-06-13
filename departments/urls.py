from rest_framework.routers import DefaultRouter
from .viewsets import DepartmentViewSet

app_name = 'departments'
router = DefaultRouter()

router.register(r"", DepartmentViewSet, "")

urlpatterns = router.urls
