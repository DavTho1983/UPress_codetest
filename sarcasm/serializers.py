from rest_framework import serializers
from .models import Headline


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headline
        fields = "__all__"