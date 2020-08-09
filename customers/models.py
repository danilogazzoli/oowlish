from django.db import models

class Customer(models.Model):
    """
    Customer's model with the attributes:
    "first_name", "last_name", "email", "gender", "company", "city", "title", "latitude", "longitude"
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(verbose_name='First_Name', max_length=50, null=False)
    last_name = models.CharField(verbose_name='Last_Name', max_length=50, null=False)
    email = models.EmailField(verbose_name='Email')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    company = models.CharField(verbose_name='Company', max_length=50)
    city = models.CharField(verbose_name='City', max_length=100)
    title = models.CharField(verbose_name='Title', max_length=100)
    latitude = models.DecimalField(verbose_name='Latitude', max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name = 'Longitude', max_digits=9, decimal_places=6)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['id']
        indexes = [
            models.Index(fields=['first_name'], name='idx_customer_first_name')
        ]
