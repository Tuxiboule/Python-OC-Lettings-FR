from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This model extends the built-in User model provided by Django to store
    additional user-related information.

    Attributes:
        user (OneToOneField): The associated user object.
        favorite_city (CharField): The user's favorite city (optional).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns:
            str: The string representation of the user profile (username).
        """
        return self.user.username
