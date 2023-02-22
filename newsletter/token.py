from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect

from six import text_type
import pyotp

class AccountPasswordResetTokenGenerator(PasswordResetTokenGenerator):
  def _make_hash_value(self, user, timestamp):
    return (
        text_type(user.uuid), text_type(timestamp), 
        text_type(user.is_active)
      )
  
  def generate_otp(self):
    self.totp = pyotp.TOTP('base32secret3232')
    return self.totp.now()
  
  def verify(self, otp):
    return self.totp.verify(otp)
  
  
account_activation_token = AccountPasswordResetTokenGenerator()
