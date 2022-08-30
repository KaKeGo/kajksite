from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
User,
Profile
)

from .serializers import (
ProfileSerializer,
)

# Create your views here.


@api_view(['GET'])
def profile_view(request, slug):
    qs = Profile.objects.filter(slug=slug)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ProfileSerializer(obj)
    return Response(serializer.data)
