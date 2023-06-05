from rest_framework.routers import SimpleRouter

from foods.views import FoodViewSet

router = SimpleRouter()
router.register(r"foods", FoodViewSet, "foods")
