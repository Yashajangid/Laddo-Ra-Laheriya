from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .utils import add_to_cart, remove_from_cart, set_qty, cart_items, totals

def view_cart(request):
    return render(request, 'cart/view.html', {'items': cart_items(request.session), 't': totals(request.session)})

@require_POST
def add(request):
    add_to_cart(request.session, int(request.POST['gig_id']), int(request.POST.get('qty',1)), request.POST.get('size','Free'))
    return redirect('cart:view')

def remove(request, key):
    remove_from_cart(request.session, key)
    return redirect('cart:view')

@require_POST
def update(request):
    key = request.POST['key']
    qty = int(request.POST['qty'])
    set_qty(request.session, key, qty)
    return redirect('cart:view')
