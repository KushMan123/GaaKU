from django.urls import re_path
from django.contrib import admin
import os

from .views import (
    FacebookWebhookView,
    )

app_name ='chatbot'
webhook_endpoint = os.getenv('webhook_endpoint')

urlpatterns = [
    re_path(f'{webhook_endpoint}', FacebookWebhookView.as_view(), name='webhook'),
]