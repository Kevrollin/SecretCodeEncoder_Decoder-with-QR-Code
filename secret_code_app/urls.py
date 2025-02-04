from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # If you were previously using encode_view and decode_view, remove them since we're using one view for both tasks.
]
