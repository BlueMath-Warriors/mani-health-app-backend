from django.urls import path
from .views import ReferralFormCreateView, ContactUsView

urlpatterns = [
    path(
        "api/referral-form",
        ReferralFormCreateView.as_view(),
        name="referral-form-create",
    ),
    path(
        "api/contact-form",
        ContactUsView.as_view(),
        name="contact-form",
    ),
]
