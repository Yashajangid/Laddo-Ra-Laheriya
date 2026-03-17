from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from gigs.models import Gig

class Command(BaseCommand):
    help = "Seed demo data"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        seller,_ = User.objects.get_or_create(username='meera', defaults={'role':'seller', 'email':'meera@example.com'})
        seller.set_password('meera'); seller.save()
        buyer,_ = User.objects.get_or_create(username='buyer', defaults={'role':'buyer','email':'buyer@example.com'})
        buyer.set_password('buyer'); buyer.save()
        data = [
            dict(title="Bandhej Lehenga", category="textiles", state="Rajasthan", price=6999, sizes="S,M,L", bestseller=True, discount=15),
            dict(title="Handmade Candle Set", category="others", state="Maharashtra", price=799, sizes="Free", bestseller=True, discount=10),
            dict(title="Kundan Necklace Set", category="jewelry", state="Gujarat", price=2499, sizes="Free"),
            dict(title="Phad Art Canvas", category="art", state="Rajasthan", price=1799, sizes="Free", bestseller=True, discount=5),
            dict(title="Block-Print Dupatta", category="textiles", state="Punjab", price=1199, sizes="Free", discount=20),
        ]
        for d in data:
            Gig.objects.get_or_create(seller=seller, title=d['title'], defaults=d)
        self.stdout.write(self.style.SUCCESS("Seeded demo users and gigs."))
