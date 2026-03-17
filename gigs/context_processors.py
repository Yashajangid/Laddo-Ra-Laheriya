from .models import Category, Gig

def global_data(request):
    states = Gig.objects.order_by().values_list('state', flat=True).distinct()
    categories = Category.objects.all()

    return {
        'CATEGORIES': categories,
        'STATES_ALL': states
    }