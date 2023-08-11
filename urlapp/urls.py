from django.urls import path
from . import views

# urlConfiguration OR API-route
urlpatterns = [
    path('check/', views.check_url)
]