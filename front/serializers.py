from rest_framework import serializers

from front.models import *


class OptionSerializer(serializers.ModelSerializer):
    value = serializers.ReadOnlyField()

    class Meta:
        model = Option
        fields = ['key', 'value']