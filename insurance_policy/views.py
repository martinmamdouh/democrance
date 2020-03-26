from rest_framework import viewsets
from insurance_policy.serializers import InsurancePolicySerializer
from insurance_policy.models import InsurancePolicy


class InsurancePolicyApi(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing insurance policy instances.
    """
    serializer_class = InsurancePolicySerializer
    queryset = InsurancePolicy.objects.all()
