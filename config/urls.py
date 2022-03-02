from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('articles/', include('Articles.urls', namespace='articles')),
    path('contact-us/', include('ContactUs.urls', namespace='contact_us')),
    path('about-us/', include('AboutUs.urls', namespace='about_us')),
    path('admin/', admin.site.urls),
    path('product/', include('Products.urls', namespace='products')), 
]


if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
