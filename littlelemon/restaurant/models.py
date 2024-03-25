from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.SmallIntegerField(default=1)
    booking_date = models.DateField()

    def __str__(self):
        return self.name + ": " + str(self.number_of_guests) + " guests on " + str(self.booking_date)


class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=1)

    def __str__(self):
        return self.title + ": " + str(self.price) + " x " + str(self.inventory)
