from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("signup/", views.signup_view, name="signup"),

    # PROFILE ROUTING
    
    path("profile/", views.profile_router, name="profile"),
    path("profile/basic/", views.profile_basic, name="profile_basic"),
    path("seller/profile/v2/", views.seller_profile_v2, name="seller_profile_v2"),
    path(
        "seller/<str:username>/",
        views.seller_public_profile,
        name="seller_public_profile"
    ),
    path("seller/gigs/new/", views.seller_upload_gig, name="seller_upload_gig"),

    path("become-seller/", views.become_seller, name="become_seller"),
    path("signout/", views.signout, name="signout"),
    

    # PASSWORD RESET
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset.html",
            email_template_name="accounts/password_reset_email.txt",
            subject_template_name="accounts/password_reset_subject.txt",
            success_url="/accounts/password-reset/done/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/accounts/reset/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
