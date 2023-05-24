from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.core.models import Games
from backend.core.serializers import GamesSerializer


class GamesDV(APIView):
    serializer_class = GamesSerializer

    def get(self, request):
        games1 = Games.objects.all()
        serializer = GamesSerializer(games1, many=True)
        return Response(serializer.data)
