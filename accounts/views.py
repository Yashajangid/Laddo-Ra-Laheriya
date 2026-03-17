from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm
from django.views.decorators.http import require_GET
from .forms import SellerProfileForm
from .models import SellerProfile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import SellerProfile
from gigs.models import Gig

User = get_user_model()

def seller_public_profile(request, username):
    seller = get_object_or_404(User, username=username)
    profile = SellerProfile.objects.filter(user=seller).first()
    gigs = Gig.objects.filter(seller=seller)

    context = {
        "seller": seller,
        "profile": profile,
        "gigs": gigs,
    }
    return render(request, "accounts/seller_public_profile.html", context)

@login_required
def seller_profile_v2(request):
    from django.contrib import messages
    from .models import SellerProfile
    from .forms import SellerProfileForm

    if getattr(request.user, "role", None) != "seller":
        messages.info(request, "Please become a seller to access the Seller Profile.")
        return redirect("accounts:become_seller")

    profile, _ = SellerProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = SellerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(
                "accounts:seller_public_profile",
                username=request.user.username
            )

    else:
        form = SellerProfileForm(instance=profile)

    return render(request, "accounts/seller_profile_v2.html", {"form": form, "profile": profile})
@require_GET    
def signout(request):
    """Log the user out via a GET (simple, conflict-free) and redirect home."""
    logout(request)
    messages.success(request, "You’ve been logged out.")
    return redirect("home")
def signup_view(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created. Please log in.')
            return redirect('accounts:login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    if request.method=='POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile saved.')
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})
@login_required
def profile_router(request):
    if getattr(request.user, "role", None) == "seller":
        return redirect("accounts:seller_profile_v2")
    return redirect("accounts:profile_basic")

@login_required
def profile_basic(request):
    return render(request, "accounts/profile.html", {})
@login_required
def seller_upload_gig(request):
    return render(request, "gigs/new.html")


@login_required
def become_seller(request):
    if getattr(request.user, "role", None) != "seller":
        request.user.role = "seller"
        request.user.save(update_fields=["role"])
        messages.success(request, "You're now a seller! Post your first gig.")
    # send them to new–gig form or back to profile
    return redirect("gigs:new")   # or: return redirect("accounts:profile")