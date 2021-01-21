from django.urls import path

from .views import CreateRequestView
from .views import RequestsView

urlpatterns = [
    path('purchase/', CreateRequestView.as_view()),
    path('', RequestsView.as_view()),
]
