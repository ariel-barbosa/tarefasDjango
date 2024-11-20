from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the Home Page!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tarefas/", include("tarefas.urls")),
]

