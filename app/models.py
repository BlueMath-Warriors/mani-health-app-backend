from django.db import models


class ReferralForm(models.Model):
    # Choices for the position field
    ADJUSTER = "Adjuster"
    EMPLOYER_OR_LAWYER = "Employer_or_Lawyer"
    POSITION_CHOICES = [
        (ADJUSTER, "Adjuster"),
        (EMPLOYER_OR_LAWYER, "Employer_or_Lawyer"),
    ]

    # Fields for the form
    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
        verbose_name="Position",
        default=ADJUSTER,
    )
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    address = models.TextField(verbose_name="Address", blank=True, null=True)
    employer_name = models.CharField(
        max_length=200, verbose_name="Employer Name", blank=True, null=True
    )
    date_of_injury = models.DateField(verbose_name="Date of Injury/Accident")
    time_of_injury = models.TimeField(
        verbose_name="Time of Injury/Accident", blank=True, null=True
    )
    location_of_injury = models.TextField(
        verbose_name="Location of Injury/Accident", blank=True, null=True
    )
    circumstances_of_injury = models.TextField(
        verbose_name="Circumstances of Injury/Accident", blank=True, null=True
    )
    insurance_company = models.CharField(
        max_length=200, verbose_name="Insurance Company"
    )
    policy_number = models.CharField(max_length=100, verbose_name="Policy Number")
    claim_number = models.CharField(max_length=100, verbose_name="Claim Number")
    adjuster_full_name = models.CharField(
        max_length=100, verbose_name="Adjuster's Full Name", blank=True, null=True
    )
    adjuster_phone_number = models.CharField(
        max_length=20, verbose_name="Adjuster's Phone Number", blank=True, null=True
    )
    adjuster_email = models.EmailField(
        verbose_name="Adjuster's Email Address", blank=True, null=True
    )

    def __str__(self):
        return f"{self.full_name} - {self.claim_number}"


class MedicalRecords(models.Model):
    referral_form = models.ForeignKey(
        ReferralForm, related_name="media_files", on_delete=models.CASCADE
    )
    media_file = models.FileField(upload_to="medical_records/")

    def __str__(self):
        return f"Medical Records of {self.referral_form.full_name}"
