# from time import sleep
# from django.core.mail import send_mail

from django import forms
from django.conf import settings
from feedback.tasks import send_feedback_email_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        """Send email using Celery task."""
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
        
        
       # Uncomment the following lines to send email directly without Celery
        # self._send_email()
       #  """Sends an email when the feedback form has been submitted."""
        # sleep(20)  # Simulate expensive operation that freezes Django
        # send_mail(
            # "Your Feedback",
            # f"\t{self.cleaned_data['message']}\n\nThank you!",
            # "support@example.com",
            # [self.cleaned_data["email"]],
            # fail_silently=False,
            #)
