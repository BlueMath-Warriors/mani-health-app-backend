from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from app.serializers import ReferralFormCreateSerializer, ContactUsSerializer
from django.template.loader import render_to_string
from common.email_engine import email_engine
from django.conf import settings


class ReferralFormCreateView(CreateAPIView):
    serializer_class = ReferralFormCreateSerializer

    def create(self, request, *args, **kwargs):
        # Use the serializer to validate the request data and save the form and media files
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            referral_form = serializer.save()
            return Response(
                {
                    "message": "Referral form created successfully!",
                    "referral_form": ReferralFormCreateSerializer(referral_form).data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactUsView(CreateAPIView):
    serializer_class = ContactUsSerializer

    def contact_us_email(self, contact_form):
        subject = "Thank you for Reaching out"
        template = "contact_email_submission.html"
        user_data = {
            "first_name": contact_form["first_name"],
            "full_name": f"{contact_form['first_name']} {contact_form['last_name']}",
            "email": contact_form["email"],
            "phone_number": contact_form["phone_number"],
            "message": contact_form["message"],
        }
        html_message = render_to_string(
            template,
            user_data,
        )
        email_engine(html_message, subject, contact_form["email"])
        subject = f"{contact_form['first_name']} Contacted!"
        admin_template = "contact_form_admin_notification.html"
        html_message = render_to_string(
            admin_template,
            user_data,
        )
        email_engine(html_message, subject, settings.SERVICE_EMAIL)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        self.contact_us_email(response.data)
        return response
