from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.response import Response

from foods.models import Food, FoodCategory, FoodListSerializer


class FoodViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        queryset = (
            FoodCategory.objects.filter(food__is_publish=True)
            .prefetch_related(Prefetch("food", queryset=Food.objects.filter(is_publish=True)), "food__additional")
            .distinct()
            .all()
        )
        serializer = FoodListSerializer(queryset, many=True)
        return Response(serializer.data)
