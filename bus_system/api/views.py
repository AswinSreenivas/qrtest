from rest_framework import generics
from rest_framework.response import Response
from .models import BusDetail, QRCode
from .serializers import BusDetailSerializer, QRCodeSerializer

class BusDetailSelectionView(generics.ListAPIView):
    serializer_class = BusDetailSerializer

    def get_queryset(self):
        qr_code_str = self.request.query_params.get('qr_code', None)
        destination = self.request.query_params.get('destination', None)

        try:
            qr_code = QRCode.objects.get(code=qr_code_str)
        except QRCode.DoesNotExist:
            return BusDetail.objects.none()

        bus_details = BusDetail.objects.filter(
            bus_stop=qr_code.bus_detail.bus_stop,
            destination=destination
        )
        return bus_details
