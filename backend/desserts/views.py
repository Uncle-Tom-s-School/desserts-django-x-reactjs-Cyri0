from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers

@api_view(["GET"])
def getDesserts(request):
    desserts = models.Dessert.objects.all()
    ser = serializers.DessertSerializer(desserts, many = True)
    return Response(ser.data)