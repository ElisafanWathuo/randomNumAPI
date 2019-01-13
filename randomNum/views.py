from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from django.shortcuts import get_object_or_404
from .serializers import RandomNumSerializer
from .models import RandomNum

def index(request):
    return render(request, 'plot/index.html', {})

class RandomNumber(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        randomNum = RandomNum.objects.all()
        serializer = RandomNumSerializer(randomNum, many=True)
        return Response(serializer.data)