from rest_framework import serializers
from .models import BusStop, BusDetail, QRCode

class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = '__all__'

class BusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusDetail
        fields = '__all__'

    def to_representation(self, instance):
        # Customize the representation of 'bus_stop' to show the name instead of the ID
        representation = super().to_representation(instance)
        representation['bus_stop'] = instance.bus_stop.name
        return representation

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = '__all__'
