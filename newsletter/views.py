from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import NewsletterForm
from .models import Newsletter 
from .token import account_activation_token

# Create your views here.
@require_POST
def subscribe(request):
    form = NewsletterForm(request.POST)
    if form.is_valid():
        user = form.save()
        current_site = get_current_site(request)
        subject = "Market Insider - Verify your Email"
        message = render_to_string("newsletter/email/welcome-email.html", {
          "user": user,
          "domain": current_site.domain,
          "uid": urlsafe_base64_encode(force_bytes(user.uuid)),
          "token": account_activation_token.make_token(user),
        })
        user.email_user(subject, message)
        
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
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = get_object_or_404(Newsletter, uuid=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True 
        user.save()
    return render(request, "newsletter/verification_successful.html")


def resubscribe(request, uid):
    user = get_object_or_404(Newsletter, uuid=uid)
    user.is_active = True 
    user.save()
    return render(request, "newsletter/resubscribed.html", {"title": "Newsletter subscription"})