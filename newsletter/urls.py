from django.urls import path

from . import views

app_name = "newsletter"

urlpatterns = [
  path("subscribe/", views.subscribe, name="subscribe"), 
  path("unsubscribe/<slug:uid>/", views.unsubscribe, name="unsubscribe"), 
  path("resubscribe/<slug:uid>/", views.resubscribe, name="resubscribe"), 
  path("verify/<slug:uidb64>/<slug:token>/", views.email_verification, name="verify"),
]