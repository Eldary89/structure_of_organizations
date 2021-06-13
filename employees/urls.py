from rest_framework.routers import DefaultRouter
from .viewsets import PositionsViewSet, EmployeeViewSet

app_name = "employees"
router = DefaultRouter()

router.register(r"positions", PositionsViewSet, "positions")
router.register(r"", EmployeeViewSet, "")

urlpatterns = router.urls
