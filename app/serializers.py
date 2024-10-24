from rest_framework import serializers
from .models import ReferralForm, MedicalRecords, ContactUs


class MedicalRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecords
        fields = ["id", "media_file"]


class ReferralFormSerializer(serializers.ModelSerializer):
    media_files = MedicalRecordsSerializer(many=True, read_only=True)

    class Meta:
        model = ReferralForm
        fields = [
            "id",
            "position",
            "first_name",
            "phone_number",
            "address",
            "employer_name",
            "date_of_injury",
            "time_of_injury",
            "location_of_injury",
            "circumstances_of_injury",
            "insurance_company",
            "policy_number",
            "claim_number",
            "adjuster_full_name",
            "adjuster_phone_number",
            "adjuster_email",
            "media_files",
        ]


class ReferralFormCreateSerializer(serializers.ModelSerializer):
    # Allow file uploads when creating a referral form
    media_files = serializers.ListField(
        child=serializers.FileField(), write_only=True, required=False
    )

    class Meta:
        model = ReferralForm
        fields = [
            "id",
            "position",
            "full_name",
            "phone_number",
            "address",
            "employer_name",
            "date_of_injury",
            "time_of_injury",
            "location_of_injury",
            "circumstances_of_injury",
            "insurance_company",
            "policy_number",
            "claim_number",
            "adjuster_full_name",
            "adjuster_phone_number",
            "adjuster_email",
            "media_files",
        ]

    def create(self, validated_data):
        media_files = validated_data.pop("media_files", [])
        referral_form = ReferralForm.objects.create(**validated_data)

        for media_file in media_files:
            MedicalRecords.objects.create(
                referral_form=referral_form, media_file=media_file
            )

        return referral_form


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ["id", "first_name", "last_name", "email", "phone_number", "message"]
