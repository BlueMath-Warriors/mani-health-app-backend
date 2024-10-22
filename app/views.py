from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import ReferralForm
from .serializers import ReferralFormCreateSerializer


# View for creating a referral form with media files
class ReferralFormCreateView(CreateAPIView):
    serializer_class = ReferralFormCreateSerializer

    def post(self, request, *args, **kwargs):
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
