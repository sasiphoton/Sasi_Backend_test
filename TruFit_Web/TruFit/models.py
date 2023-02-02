from django.db import models

OPTION = (
    ("SuperAdmin", "SuperAdmin"),
    ("Admin", "Admin"),
    ("SalesEngineer", "SalesEngineer"),
    ("AccountManager", "AccountManager"),
)


# Create your models here.
class TFUser(models.Model):
    """
    This class is used to main the TruFit app user information.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=OPTION, default="Admin")
    active_role = models.CharField(max_length=20, choices=OPTION, default="SalesEngineer")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

