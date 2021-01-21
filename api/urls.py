from django.urls import include
from django.urls import path

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('book_data/', include('book_data.urls')),
    path('requests/', include('purchase.urls')),
]