from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.core.files.storage import default_storage


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Gig(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="gigs"
    )

    title = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="gigs"
    )

    state = models.CharField(max_length=100, default="Rajasthan")

    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    

    description = models.TextField(blank=True)
    tags = models.CharField(max_length=200, blank=True)

    image = models.ImageField(upload_to="gigs/", blank=True, null=True)
    bestseller = models.BooleanField(default=False)

    discount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    @property
    def total_stock(self):
        return sum(size.quantity for size in self.sizes.all())

    def price_after_discount(self):
        if self.discount:
            return int(self.price * (100 - self.discount) / 100)
        return self.price

    @property
    def image_url(self):
        try:
            if self.image and default_storage.exists(self.image.name):
                return self.image.url
        except Exception:
            pass
        return static("img/p1.png")
class GigSize(models.Model):
    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
        ("FREE", "Free Size"),
    ]

    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, related_name="sizes")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.gig.title} - {self.size} ({self.quantity})"

