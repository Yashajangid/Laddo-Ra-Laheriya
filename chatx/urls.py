from django.urls import path
from . import views

app_name = 'chatx'
urlpatterns = [
    path('<int:gig_id>/', views.room, name='room'),
    path('<int:gig_id>/list/', views.list_messages, name='list'),
    path('<int:gig_id>/send/', views.send_message, name='send'),
]
