from django.urls import path
from . import views
from .views import new_gig
app_name = 'gigs'
urlpatterns = [
    path("categories/", views.categories, name="categories"),
    path('', views.gig_list, name='list'),
    path('<int:pk>/', views.gig_detail, name='detail'),
    path("new/", new_gig, name="new"),
    path('new/', views.gig_new, name='new'),
]
