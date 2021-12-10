from rest_framework import serializers
from users.models import Pocket

class PocketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pocket
        fields = '__all__'