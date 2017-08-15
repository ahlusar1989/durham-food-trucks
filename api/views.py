from django.http import JsonResponse

from api.models import Truck


def index(request):
    return JsonResponse({'yo': 'whats up'})


def data(request):
    trucks = Truck.objects.filter(location__isnull=False)
    return JsonResponse({'trucks': [t.to_dict() for t in trucks]})