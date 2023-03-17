from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.sites.shortcuts import get_current_site

from .forms import NewsletterForm
from .models import Newsletter 
from .emails import verify_email
from .emails import send_newsletter_email

# Create your views here.
@require_POST
def subscribe(request):
    form = NewsletterForm(request.POST)
    if form.is_valid():
        user = form.save()
        current_site = get_current_site(request)
        send_newsletter_email(user, current_site)
        return render(request, "newsletter/thanks.html", {"title": "Newsletter subscription"})
    else:
        for error in form.errors.values():
            messages.info(request, error)
        return redirect(request.META["HTTP_REFERER"])


def unsubscribe(request, uid):
  subscriber = get_object_or_404(Newsletter, uuid=uid)
  subscriber.is_active = False 
  subscriber.save()
  context = {
      "title": "Newsletter Unsubscribe", 
      "uid": subscriber.uuid,
  }
  return render(request, "newsletter/unsubscribe.html", context)


def email_verification(request, uidb64, token):
    verify_email(uidb64, token)
    return render(request, "newsletter/verification_successful.html")


def resubscribe(request, uid):
    user = get_object_or_404(Newsletter, uuid=uid)
    user.is_active = True 
    user.save()
    return render(request, "newsletter/resubscribed.html", {"title": "Newsletter subscription"})