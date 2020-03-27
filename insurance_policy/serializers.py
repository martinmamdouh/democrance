from rest_framework import serializers
from insurance_policy.models import InsurancePolicy


class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = ["__all__"]
