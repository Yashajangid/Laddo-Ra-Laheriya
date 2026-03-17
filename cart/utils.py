from gigs.models import Gig

def get_cart(session):
    return session.setdefault('cart', {})

def add_to_cart(session, gig_id, qty=1, size='Free'):
    cart = get_cart(session)
    key = f"{gig_id}:{size}"
    cart[key] = cart.get(key, 0) + qty
    session.modified = True

def remove_from_cart(session, key):
    cart = get_cart(session)
    if key in cart:
        del cart[key]
        session.modified = True

def set_qty(session, key, qty):
    cart = get_cart(session)
    if key in cart:
        cart[key] = max(1, qty)
        session.modified = True

def cart_items(session):
    cart = get_cart(session)
    items = []
    for key, qty in cart.items():
        gid, size = key.split(':',1)
        g = Gig.objects.get(pk=int(gid))
        items.append({'key': key, 'gig': g, 'qty': qty, 'size': size, 'subtotal': g.price_after_discount()*qty})
    return items

def totals(session):
    items = cart_items(session)
    subtotal = sum(i['subtotal'] for i in items)
    return {'subtotal': subtotal, 'discount': 0, 'grand': subtotal}
