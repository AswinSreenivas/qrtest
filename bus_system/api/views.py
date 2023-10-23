from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import QRCode
from .serializers import QRCodeSerializer, BusDetailSerializer  # Import BusDetailSerializer
from rest_framework.response import Response

class BusDetailByQRCodeView(generics.RetrieveAPIView):
    serializer_class = QRCodeSerializer

    def retrieve(self, request, *args, **kwargs):
        qr_code_str = request.data.get('qr_code')  # Assuming the QR code is posted as 'qr_code' in the request data
        try:
            qr_code = QRCode.objects.get(code=qr_code_str)
        except QRCode.DoesNotExist:
            return Response({"detail": "QR code not found"}, status=404)

        bus_detail = qr_code.bus_detail
        bus_detail_serializer = BusDetailSerializer(bus_detail)
        return Response(bus_detail_serializer.data)
