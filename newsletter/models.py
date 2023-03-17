from django.db import models
import uuid

# Create your models here.
class Newsletter(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(max_length = 254, unique=True, error_messages={"email": "Email already subscribed!"})
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    