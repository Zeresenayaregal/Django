from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="OIP.jfif", upload_to='profile_pics')

    def __str__(self):
        return super().__str__()  # or f"{self.user.username}"
    def save(self):
        super().save()

        img = Image.open(self.image.path)
         
        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
