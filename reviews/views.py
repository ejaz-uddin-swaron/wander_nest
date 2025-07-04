# reviews/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

class ReviewListView(APIView):
    def get(self, request):
        reviews = Review.objects.all().order_by('-date')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
