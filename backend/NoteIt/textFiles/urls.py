from django.urls import path
from .views import textFilesView, textFilesPut


urlpatterns = [
    path('api/create', textFilesPut.as_view()),
    path('api/get', textFilesView.as_view())
]
