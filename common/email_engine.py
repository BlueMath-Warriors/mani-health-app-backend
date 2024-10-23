from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From
from django.conf import settings


def email_engine(
    html_message, subject, recipient, email_title="Almani Health Institire"
):
    """
    Sends an email using the SendGrid service.

    This function attempts to send an email with the given HTML content, subject, recipient email,
    and title. It retries sending the email up to a specified number of times if it fails.

    Parameters:
    html_message (str): The HTML content of the email.
    subject (str): The subject of the email.
    recipient (str): The recipient's email address.
    email_title (str): The title of the email.

    Returns:
    bool: True if the email was sent successfully, False otherwise.

    from django.template.loader import render_to_string
    html_message = render_to_string(
        template,
        {
           key: value
        },
    )
    """

    number_of_remaining = 0
    email_sent = False

    while not email_sent and number_of_remaining < settings.EMAIL_TRIES:
        try:
            message = Mail(
                to_emails=recipient,
                subject=subject,
                html_content=html_message,
            )
            message.from_email = From(settings.SERVICE_EMAIL, email_title)
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            sg.send(message)
            email_sent = True
        except Exception as exc:
            print(f"Exception in sending email {exc}")
        number_of_remaining += 1

    return email_sent
