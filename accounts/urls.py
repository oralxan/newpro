from django.urls import path 
from .views import SignUpView
urlpatterns = [
    path('Signup/', SignUpView.as_view(),name='signu')
]
