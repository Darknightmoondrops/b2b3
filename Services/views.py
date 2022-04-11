from django.shortcuts import render

def services_list_page(request):



    return render(request,'Services/services_list_page/services_list_page.html')


def service_detail_page(request,id,slug):

    return render(request,'Services/service_detail_page/service_detail_page.html')