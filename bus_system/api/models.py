from django.db import models

# Create your models here.
class BusStop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)  # Add a field to store the location of the bus stop, e.g., coordinates, address, etc.
    # Add other fields as needed, such as a description, image, or any other relevant information.enth venengilum add aakam

    def __str__(self):
        return self.name


class BusDetail(models.Model):
    bus_stop = models.ForeignKey(BusStop, on_delete=models.CASCADE)
    timing = models.DateTimeField()
    destination = models.CharField(max_length=100)
    fare = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.bus_stop.name} to {self.destination} at {self.timing}"



class QRCode(models.Model):
    code = models.CharField(max_length=100, unique=True)
    bus_detail = models.ForeignKey(BusDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
