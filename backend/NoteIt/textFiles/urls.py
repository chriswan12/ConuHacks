from django.urls import path
from .views import textFilesView


urlpatterns = [
    path('api/create', textFilesView.as_view())
]
