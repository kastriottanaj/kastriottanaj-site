from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # ✅ route for /contact/
    path('contact/success/', views.contact_success,
         name='contact-success'),  # ✅ route for thank-you page
    path("imprint/", views.imprint, name="imprint"),  # ✅ route for /imprint/
]
