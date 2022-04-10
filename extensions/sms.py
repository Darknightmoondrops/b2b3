from SiteSettings.models import SiteSettings
from .melipayamak import Api


def send_sms(phone,text):
    settings: SiteSettings = SiteSettings.objects.first()
    username = f'{settings.melipayamak_username}'
    password = f'{settings.melipayamak_password}'
    api = Api(username,password)
    sms = api.sms()
    to = f'{phone}'
    _from = f'{settings.melipayamak_phone}'
    text = f'{text}'
    response = sms.send(to,_from,text)
