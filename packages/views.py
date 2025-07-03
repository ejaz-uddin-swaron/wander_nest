from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Package
from .serializers import PackageSerializer

class PackageListView(APIView):
    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
