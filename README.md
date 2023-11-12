# qrtest
 
THish is what views.py does 
We retrieve the posted QR code from request.data assuming it's posted as 'qr_code' in the request data.

We attempt to find a QRCode object in the database that matches the posted QR code.

If the QR code is not found, we return a 404 Not Found response with a message indicating that the QR code was not found.

If the QR code is found, we retrieve the associated BusDetail and serialize it using the BusDetailSerializer.
