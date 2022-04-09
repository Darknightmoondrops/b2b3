from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('Home.urls',namespace='home')),
    # Articles Url
    path('articles/', include('Articles.urls')),
    path('api/articles/', include('Articles.api_urls')),
    # Products Url
    path('products/', include('Products.urls')),
    path('api/products/', include('Products.api_urls')),
    # UserPanel Url
    path('user-panel/',include('UserPanel.urls')),

    # Site Settings Url
    path('api/site-settings/', include('SiteSettings.api_urls')),
    # ContactUs Url
    path('contact-us/', include('ContactUs.urls')),
    path('api/contact-us/', include('ContactUs.api_urls')),
    # AboutUs Url
    path('about-us/', include('AboutUs.urls')),
    path('api/about-us/', include('AboutUs.api_urls')),

    # SocialNetworks Url
    path('api/social-networks/',include('SocialNetworks.api_urls')),

    # Admin
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
