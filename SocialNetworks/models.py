from django.db import models

class SocialNetworks(models.Model):
    instagram = models.URLField(verbose_name="Instagram")
    whatsapp = models.URLField(verbose_name="Whatsapp")
    youtube = models.URLField(verbose_name="Youtube")
    telegram = models.URLField(verbose_name="Telegram")
    facebook = models.URLField(verbose_name="Facebook")