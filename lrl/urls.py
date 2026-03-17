from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from gigs.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("gigs/", include(("gigs.urls", "gigs"), namespace="gigs")),

    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('chat/', include('chatx.urls')),
    
]


if settings.DEBUG:
    # Serve uploaded media in dev
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Serve project static files in dev (point to STATICFILES_DIRS[0])
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])