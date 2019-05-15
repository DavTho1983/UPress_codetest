from rest_framework import generics

from .models import Headline
from .serializers import ResultSerializer

# Create your views here.
class ResultAPIListView(generics.ListAPIView):
    queryset = Headline.objects.all()
    serializer_class = ResultSerializer


class ResultAPIID(generics.RetrieveAPIView):
    queryset = Headline.objects.all()
    serializer_class = ResultSerializer