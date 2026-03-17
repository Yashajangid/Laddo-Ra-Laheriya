from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from gigs.models import Gig
from .models import ChatMessage

@login_required
def room(request, gig_id):
    gig = get_object_or_404(Gig, pk=gig_id)
    return render(request, 'chat/room.html', {'gig': gig})

@login_required
def list_messages(request, gig_id):
    gig = get_object_or_404(Gig, pk=gig_id)
    msgs = ChatMessage.objects.filter(gig=gig).values('id','sender__username','text','created_at')
    return JsonResponse({'messages': list(msgs)})

@login_required
def send_message(request, gig_id):
    gig = get_object_or_404(Gig, pk=gig_id)
    text = request.POST.get('text','').strip()
    if text:
        ChatMessage.objects.create(gig=gig, sender=request.user, text=text)
    return JsonResponse({'ok': True})
