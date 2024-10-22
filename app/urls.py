from django.urls import path
from .views import ReferralFormCreateView

urlpatterns = [
    path(
        "api/referral-form",
        ReferralFormCreateView.as_view(),
        name="referral-form-create",
    ),
]
