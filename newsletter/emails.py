from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from .token import account_activation_token
from .models import Newsletter


def send_newsletter_email(user, current_site):
    context = {
      "user": user,
      "domain": current_site.domain,
      "uid": urlsafe_base64_encode(force_bytes(user.uuid)),
      "token": account_activation_token.make_token(user),
    }
    
    subject = "Market Insider - Verify your Email"
    message = render_to_string("newsletter/email/welcome-email.html", context)
    return send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,[user.email], fail_silently=True)


def verify_email(uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = get_object_or_404(Newsletter, uuid=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True 
        user.save()
    return user