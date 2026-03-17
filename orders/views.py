from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal, ROUND_HALF_UP
from cart.utils import cart_items, totals
from .models import Order, OrderItem
import razorpay

@login_required
def checkout(request):
    # Build items/totals from session
    items = cart_items(request.session)
    if not items:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart:view')

    t = totals(request.session)

    # Create order now (single-screen flow)
    order = Order.objects.create(buyer=request.user, total_amount=t['grand'])
    for i in items:
        OrderItem.objects.create(
            order=order, gig=i['gig'], qty=i['qty'], size=i['size'],
            price=i['gig'].price_after_discount()
        )

    # Prepare Razorpay order if keys present
    key_id = settings.RAZORPAY_KEY_ID
    key_secret = settings.RAZORPAY_KEY_SECRET
    rzp_amount_paise = None
    if key_id and key_secret:
        try:
            client = razorpay.Client(auth=(key_id, key_secret))
            total_rupees = Decimal(order.total_amount)
            rzp_amount_paise = int((total_rupees * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
            rp_order = client.order.create({
                "amount": rzp_amount_paise,
                "currency": settings.CURRENCY,
                "receipt": f"lrl_{order.id}",
                "payment_capture": 1
            })
            order.razorpay_order_id = rp_order["id"]
            order.save()
        except Exception as e:
            messages.error(request, f"Could not create Razorpay order: {e}")

    # Keep cart until payment/COD completes
    return render(request, "orders/checkout.html", {
        "order": order,
        "items": items,
        "t": t,
        "razorpay_key": key_id,
        "rzp_amount_paise": rzp_amount_paise,
    })

@csrf_exempt
@login_required
def payment_success(request, order_id):
    # Mark paid after Razorpay handler posts back
    order = get_object_or_404(Order, pk=order_id, buyer=request.user)
    order.razorpay_payment_id = request.POST.get('razorpay_payment_id','')
    order.razorpay_signature  = request.POST.get('razorpay_signature','')
    order.status = 'paid'
    order.save()
    # Clear cart AFTER success
    request.session['cart'] = {}
    messages.success(request, f'Payment successful for Order #{order.id}.')
    return redirect('orders:detail', order_id=order.id)

@login_required
def cod_place_order(request, order_id):
    # COD confirmation form posts here
    order = get_object_or_404(Order, pk=order_id, buyer=request.user)
    order.status = "cod"
    order.save()
    # Clear cart AFTER COD placement (change this if you want to keep cart items)
    request.session["cart"] = {}
    messages.success(request, f"Order #{order.id} placed with Cash on Delivery.")
    return redirect("orders:detail", order_id=order.id)

@login_required
def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id, buyer=request.user)
    return render(request, 'orders/detail.html', {'order': order})
