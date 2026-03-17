from django.db import models
from django.conf import settings
from gigs.models import Gig

class Order(models.Model):
    STATUS = (('pending','Pending'), ('paid','Paid'), ('failed','Failed'))
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
    max_length=20,
    choices=[("pending", "Pending"), ("paid", "Paid"), ("cod", "Cash on Delivery")],
    default="pending"
)

    total_amount = models.PositiveIntegerField(default=0)
    razorpay_order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    razorpay_signature = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.buyer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    gig = models.ForeignKey(Gig, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=20, default='Free')
    price = models.PositiveIntegerField()  # snapshot price

    def subtotal(self):
        return self.price * self.qty
