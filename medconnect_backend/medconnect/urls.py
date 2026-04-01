
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "status": "MedConnect Backend Running 🚀"
    })

urlpatterns = [
    path('', home),
    path('api/', include('core.urls')),
]