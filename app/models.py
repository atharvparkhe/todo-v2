from django.db import models
from base.models import BaseModel
from authentication.models import UserModel

class TodoModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)