# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from .models import SellerProfile

User = get_user_model()

ROLE_CHOICES = (
    ("buyer", "Buyer"),
    ("seller", "Seller"),
)

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = [
            "display_name",
            "phone",
            "address",
            "city",
            "state",
            "postal_code",
            "craft_specialization",
            "avatar",
            "instagram",
            "whatsapp",
            "linkedin",
            "public_email",
            "website",
        ]
        widgets = {
            "display_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter display name"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter mobile number"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter street address"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter city"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter state"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter postal code"}),
            "craft_specialization": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your craft(s)"}),
             "instagram": forms.TextInput(attrs={
                "class": "field",
                "placeholder": "@username"
            }),
            "twitter": forms.TextInput(attrs={
                "class": "field",
                "placeholder": "@username"
            }),
            "linkedin": forms.URLInput(attrs={
                "class": "field",
                "placeholder": "https://linkedin.com/in/..."
            }),
            "whatsapp": forms.TextInput(attrs={
                "class": "field",
                "placeholder": "+91 XXXXX XXXXX"
            }),
            "public_email": forms.EmailInput(attrs={
                "class": "field",
                "placeholder": "contact@email.com"
            }),
        }
class PrettyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your email'}
        )
    )
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="We’ll send order updates here.")

    class Meta:
        model = User
        # Base fields that always exist on Django's User/AbstractUser
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    """
    Edit basic profile info. If your User model has a `role` field,
    it will be included automatically.
    """
    class Meta:
        model = User
        base_fields = ["first_name", "last_name", "email"]
        # If your custom user has 'role', include it.
        if hasattr(User, "role"):
            fields = base_fields + ["role"]
        else:
            fields = base_fields
class SignupForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your full name",
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email",
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Choose a username",
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Create a password",
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirm your password",
        })
    )
    # Optional: only include if your User model has a `role` field
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=False,
        widget=forms.Select()
    )

    class Meta:
        model = User
        fields = ("full_name", "email", "username", "password1", "password2", "role")

    def save(self, commit=True):
        user = super().save(commit=False)
        # Split full_name into first/last (simple heuristic)
        full_name = self.cleaned_data.get("full_name", "").strip()
        if " " in full_name:
            user.first_name, user.last_name = full_name.split(" ", 1)
        else:
            user.first_name = full_name

        user.email = self.cleaned_data["email"]

        # Save role if your User model has this field
        role = self.cleaned_data.get("role")
        if role and hasattr(user, "role"):
            user.role = role

        if commit:
            user.save()
        return user
