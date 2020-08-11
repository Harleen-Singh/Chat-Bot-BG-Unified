from django.urls import path
from .views import *
urlpatterns=[
    path('predictResponse/',Predict.as_view())
]