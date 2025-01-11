from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.generate_readme_from_github, name="generate_readme"),  # Ensure this is the main root route
]
