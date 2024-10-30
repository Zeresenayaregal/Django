from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="OIP.jfif", upload_to='profile_pics')

    def __str__(self):
        return super().__str__()  # or f"{self.user.username}"