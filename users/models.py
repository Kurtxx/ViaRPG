from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Resources(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stat_lvl = models.IntegerField(default=1)
    stat_minexp = models.IntegerField(default=1)
    stat_maxexp = models.IntegerField(default=200)
    stat_str = models.IntegerField(default=3)
    stat_vit = models.IntegerField(default=2)
    stat_dex = models.IntegerField(default=3)
    stat_money = models.IntegerField(default=100)
    stat_food = models.IntegerField(default=1000)
    stat_energy = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Statystyki'

    def save(self, **kwargs):
        super().save()
