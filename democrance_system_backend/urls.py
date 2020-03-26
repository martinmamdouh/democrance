
from django.contrib import admin
from django.urls import path, include
from customer.views import CustomerApi
from insurance_policy.views import InsurancePolicyApi

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('custom_jwt.urls')),
    path('api/v1/create_customer/', CustomerApi.as_view(
        {"post": "create"})),
    path('api/v1/create_policy/', InsurancePolicyApi.as_view(
        {"post": "create"}))

]
