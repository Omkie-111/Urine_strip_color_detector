from django.urls import path
from .views import analyze_urine_strip, result

urlpatterns = [
    path('', analyze_urine_strip, name='process_image'),
    path('result/<int:pk>/', result, name='result'),
]
