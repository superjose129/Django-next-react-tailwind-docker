from rest_framework import serializers
from char_count import models


class CharCountSerializer(serializers.Serializer):
    class Meta:
        model = models.CharCount
        field = ["char_count"]
