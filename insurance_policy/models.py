from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from customer.models import Customer


class InsurancePolicy(models.Model):
    type = models.CharField(max_length=50, null=False, blank=False)
    premium = models.IntegerField(null=False, blank=False, validators=[
                                  MinValueValidator(0, "premium field should be an interger number greater than Zero.")])
    cover = models.IntegerField(null=False, blank=False, validators=[
        MinValueValidator(
            0, "cover field should be an interger number greater than Zero.")])
    customer = models.OneToOneField(
        Customer, on_delete=models.PROTECT,  null=False, blank=False)

    class Meta:
        db_table = 'insurance_policy'

    def __str__(self):
        return self.premium
