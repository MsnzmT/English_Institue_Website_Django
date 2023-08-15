from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model



User = get_user_model()

@receiver(post_save, sender=User, dispatch_uid='save_new_user_cart')
def save_new_user_cart(sender, instance, created, **kwargs):
    if created:
        from .models import cart
        cart.objects.create(user=instance)