from django.http import JsonResponse
from django.views.decorators.http import require_GET
@require_GET
def test_view(request):
    return JsonResponse({'message':'Hello'})