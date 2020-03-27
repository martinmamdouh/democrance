from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
