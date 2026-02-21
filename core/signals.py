from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sale


@receiver(post_save, sender=Sale)
def update_stock(sender, instance, created,  **kwargs):
    if created:
        product = instance.product
        product.stock_quantity -= instance.quantity
        product.save()