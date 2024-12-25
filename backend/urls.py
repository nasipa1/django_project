from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home view for testing
def home_view(request):
    return HttpResponse("<h1>Welcome to the Django Backend</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include URLs from the API app
    path('', home_view, name='home'),
]
