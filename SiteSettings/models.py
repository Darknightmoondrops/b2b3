from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, blank=False, default="some string",verbose_name="Site Name",)
    payment_token = models.CharField(max_length=300, blank = False, default="some string",verbose_name='Payment Token')
    site_description = models.TextField(default="some string",verbose_name='Site Description')
    keyword = models.TextField(default="some string",verbose_name='Keyword')
    logo = models.ImageField(upload_to="logo/v1",verbose_name='Logo')
    contact_number = models.CharField(max_length=15, default='123',verbose_name='Contact number')
    address = models.TextField(null=False, default="some string",verbose_name='Address')
    email = models.EmailField(default='django@mail.com',verbose_name='Email')
    instagram_link = models.URLField(default='instalink',verbose_name="Instagram")
    android_application_link = models.URLField(default="some string",verbose_name="Android Application")

    def __str__(self):
        return f'{self.site_name}'