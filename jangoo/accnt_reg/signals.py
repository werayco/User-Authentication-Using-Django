from django.dispatch import receiver
from .forms import UserRegform
from django.db.models.signals import post_save, post_delete
# from .emailer import send_email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr
from django.contrib.auth import get_user_model

User_model= get_user_model()

def send_email(recipient_email, subject, body):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(("screenbond", "screenbondhq@gmail.com"))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the HTML body with the embedded image
        msg.attach(MIMEText(body, 'html'))

        # Set up the SMTP server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login("screenbondhq@gmail.com", "ryyodmxmnryxojiz")

        # Send the email
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {str(e)}")


@receiver(post_save, sender=User_model)
def signal_handler(sender, instance, created, **kwargs):
    if created:
            print("added")
            
            
            body = f"""
                Hi {instance.username},
            Thanks for registering into the Screenbond database! We're thrilled to have you with us.

            Be sure to follow us on social media to stay updated:
            - TikTok: [@screenbond](https://www.tiktok.com/@screenbond)
            - Instagram: [@screenbond](https://www.instagram.com/screenbond)
            - YouTube: [@screenbond](https://www.youtube.com/screenbond)

            We look forward to connecting with you!

            Best Regards,
            The Screenbond Team
    """
            subject = f"{instance.username}, Welcome! This is Screenbond!"
            send_email(instance.email,subject,body)

    else:
        print("there is nothing here!") 

@receiver(post_delete, sender=UserRegform)
def sig_handler_for_pDel(sender, instance, using, **kwargs):
    pass
