from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('Home.urls',namespace='home')),
    path('articles/', include('Articles.urls')),
    path('api/articles/', include('Articles.api_urls')),
    path('contact-us/', include('ContactUs.urls')),
    path('about-us/', include('AboutUs.urls')),
    path('products/', include('Products.urls')),
    path('api/products/', include('Products.api_urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
