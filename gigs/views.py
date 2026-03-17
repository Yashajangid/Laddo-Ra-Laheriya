from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Gig, Category

from django.shortcuts import render
from django.utils.text import slugify
from .models import Gig
from .forms import GigForm

# gigs/views.py
from .forms import GigSizeFormSet
from django.db.models import F, Value, IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render

from .models import Gig, Category, GigSize  # adjust if your names differ

PLACEHOLDER = "https://images.unsplash.com/photo-1549880338-65ddcdfd017b?q=80&w=1200&auto=format&fit=crop"

def categories(request):
    qs = Gig.objects.select_related("category").all()

    # filters
    q = request.GET.get("q", "").strip()
    if q:
        qs = qs.filter(title__icontains=q)

    cat_slug = request.GET.get("category")
    if cat_slug:
        qs = qs.filter(category__slug=cat_slug)

    state = request.GET.get("state")
    if state:
        qs = qs.filter(city__iexact=state)  # or adjust to your data model

    # build lightweight cards payload
    gigs = []
    for g in qs:
        # price/discount – adapt if your fields have other names
        price = getattr(g, "price", 0) or 0
        sale_price = getattr(g, "sale_price", None)
        discount_percent = None
        if sale_price and price and sale_price < price:
            discount_percent = round((price - sale_price) * 100 / price)

        image_url = getattr(g, "image_url", None)
        if not image_url and hasattr(g, "image") and getattr(g.image, "url", None):
            image_url = g.image.url
        image_url = image_url or PLACEHOLDER

        gigs.append({
            "id": g.id,
            "title": g.title,
            "price_display": f"{sale_price or price:,}".replace(",", ","),  # ₹ formatting is done in template
            "city": getattr(g, "city", "Jaipur"),
            "category_name": getattr(g.category, "name", "Craft"),
            "image_url": image_url,
            "discount_percent": discount_percent,
        })

    categories = Category.objects.order_by("name").values("name", "slug")
    states = (
        Gig.objects.exclude(city__isnull=True)
        .exclude(city__exact="")
        .order_by("city").values_list("city", flat=True).distinct()
    )

    return render(request, "gigs/categories.html", {
        "gigs": gigs,
        "categories": categories,
        "states": states,
    })

def home(request):
    q = request.GET.get('q','')
    gigs = Gig.objects.all().order_by('-created_at')
    if q:
        gigs = gigs.filter(Q(title__icontains=q)|Q(description__icontains=q)|Q(tags__icontains=q)|Q(state__icontains=q))
    best = Gig.objects.filter(bestseller=True)[:12]
    deals = Gig.objects.filter(discount__gt=0)[:12]
    states = Gig.objects.order_by().values_list('state', flat=True).distinct()
    ctx = {'gigs': gigs[:12], 'best': best, 'deals': deals, 'states': states}
    return render(request, 'home.html', ctx)

def gig_list(request):
    qs = Gig.objects.all().order_by('-created_at')
    cat = request.GET.get('category'); state = request.GET.get('state'); q = request.GET.get('q')
    if cat: qs = qs.filter(category=cat)
    if state: qs = qs.filter(state__iexact=state)
    if q: qs = qs.filter(Q(title__icontains=q)|Q(description__icontains=q)|Q(tags__icontains=q))
    return render(request, 'gigs/list.html', {'gigs': qs})

def gig_detail(request, pk):
    g = get_object_or_404(Gig, pk=pk)
    return render(request, 'gigs/detail.html', {'gig': g})
@login_required
def new_gig(request):
    if request.method == "POST":
        form = GigForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("gigs:list")  # or wherever you want
    else:
        form = GigForm()

    return render(request, "gigs/new.html", {"form": form})
@login_required
def gig_new(request):
    if not request.user.is_seller():
        messages.error(request,'Only sellers can post gigs.')
        return redirect('gigs:list')
    if request.method=='POST':
        data = request.POST
        g = Gig(
            seller=request.user,
            title=data.get('title','Untitled'),
            category=data.get('category','others'),
            state=data.get('state','Rajasthan'),
            price=int(data.get('price', '999')),
            stock=int(data.get('stock','10')),
            sizes=data.get('sizes','Free'),
            description=data.get('description',''),
            tags=data.get('tags',''),
            bestseller=bool(data.get('bestseller')),
            discount=int(data.get('discount','0')),
        )
        
        if request.FILES.get('image'):
            g.image = request.FILES['image']
        g.save()
        messages.success(request,'Gig posted.')
        return redirect('gigs:detail', pk=g.pk)
    return render(request, 'gigs/new.html', {'categories': categories})
from .forms import GigForm

@login_required
def new_gig(request):
    if request.method == "POST":
        form = GigForm(request.POST, request.FILES)
        if form.is_valid():
            gig = form.save(commit=False)
            gig.seller = request.user
            gig.save()

            # save sizes + quantities
            sizes = request.POST.getlist("size[]")
            quantities = request.POST.getlist("quantity[]")

            for s, q in zip(sizes, quantities):
                if s and q:
                    GigSize.objects.create(
                        gig=gig,
                        size=s,
                        quantity=int(q)
                    )

            return redirect("gigs:detail", pk=gig.pk)
    else:
        form = GigForm()

    # ✅ THIS RETURN FIXES YOUR ERROR
    return render(request, "gigs/new.html", {"form": form})