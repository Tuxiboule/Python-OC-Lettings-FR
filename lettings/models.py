from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    A model representing a physical address.

    Attributes:
        number (PositiveIntegerField): The street number of the address.
        street (CharField): The name of the street.
        city (CharField): The city where the address is located.
        state (CharField): The state where the address is located (abbreviated).
        zip_code (PositiveIntegerField): The ZIP code of the address.
        country_iso_code (CharField): The ISO code of the country where the address is located.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns:
            str: The string representation of the address.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    A model representing a letting property
    Attributes:
        title (CharField): The title of the letting.
        address (OneToOneField): The address associated with the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns:
            str: The string representation of the letting.
        """
        return self.title
