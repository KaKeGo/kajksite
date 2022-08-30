from django.urls import path

from .views import (
profile_view,
)

app_name = 'accounts'

urlpatterns = [
    path('profile/<slug:slug>', profile_view, name='profile'),
]
