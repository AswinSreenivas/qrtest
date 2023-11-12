from django.db import models

class BusStop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='bus_stop_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class BusDetail(models.Model):
    bus_stop = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    timing = models.DateTimeField()
    destination = models.CharField(max_length=100)
    fare = models.DecimalField(max_digits=5, decimal_places=2)
    capacity = models.PositiveIntegerField(default=50)  # Add a field to represent the bus capacity

    def __str__(self):
        return f"{self.bus_stop.name} to {self.destination} at {self.timing}"

class QRCode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    bus_detail = models.OneToOneField(BusDetail, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Add a timestamp for when the QR code is created

    def __str__(self):
        return self.code
