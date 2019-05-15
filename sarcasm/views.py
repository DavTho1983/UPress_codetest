from rest_framework import generics

from .models import Headline
from .serializers import HeadlineSerializer

# Create your views here.
class HeadlineAPIListView(generics.ListAPIView):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer


class HeadlineAPIID(generics.RetrieveAPIView):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer