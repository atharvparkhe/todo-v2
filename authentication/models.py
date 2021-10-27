from django.db import models
from base.models import *

class UserModel(BaseUser):
    def __str__(self):
        return self.email

class OTPModel(BaseModel):
    otp = models.IntegerField()
    is_valid = models.BooleanField(default=False)
    expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)