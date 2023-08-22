from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import cart


User = get_user_model()

@receiver(post_save, sender=User, dispatch_uid='save_new_user_cart')
def save_new_user_cart(sender, instance, created, **kwargs):
    if created:
        from .models import cart
        cart.objects.create(user=instance)
        

@receiver(pre_save, sender=cart, dispatch_uid='save_cart_before_edit')
def save_cart_before_edit(sender, instance, **kwargs):
    if instance.pk:
        instance.final_price = instance.price
        instance.discount_price = 0
        if instance.discount:
            discount_price = instance.price * instance.discount.percent / 100
            instance.discount_price = discount_price
            instance.final_price = instance.price - discount_price