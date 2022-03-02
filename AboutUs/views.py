from django.shortcuts import render
from .models import AboutUs


"""

Views :

    aboutus_page() # Show About Us
    
"""


def aboutus_page(request):
    aboutus = AboutUs.objects.last()
    
    context = {
        'aboutus': aboutus,
    }
    
    return render(request,'AboutUs/aboutus_page/aboutus_page.html',context)