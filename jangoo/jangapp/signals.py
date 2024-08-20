from django.dispatch import receiver
from .models import posts
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=posts)
def signal_handler(sender, instance, created, **kwargs):
    if created:
        print(
            f"{instance.name} record was added to the {sender.__name__} database"
        )  # sender.__name__ will return the name of the model that sent the signal
    else:
        print("there is nothing here!")

@receiver(post_delete, sender=posts)
def sig_handler_for_pDel(sender, instance, using, **kwargs):
    pass
