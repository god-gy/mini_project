from django.urls import path
from . import views

app_name = "blessings"

urlpatterns = [
    path("", views.home, name="home"),
    path("write/", views.write, name="write"),
    path("owner/inbox/", views.owner_inbox, name="owner_inbox"),
]
