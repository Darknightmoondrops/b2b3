from django.contrib.auth import authenticate,login,logout
from CustomizedUserModel.models import Userperson
from SiteSettings.models import SiteSettings
from Products.models import ProductsComments
from django.shortcuts import render,redirect
from VerificationCodes.models import Codes
from django.contrib import messages
from extensions.sms import send_sms
from random import randint
from extensions.permission import is_user


def userpanel_page(request):
    if is_user(request) == True:

        products_comments = ProductsComments.objects.filter(user_id=request.user.id).all()
        site_settings = SiteSettings.objects.last()
        title = site_settings.site_name + " - " + "پنل کاربری"
        context = {
            'title': title,
            'products_comments': products_comments,
        }
        return render(request,'UserPanel/userpanel_page/userpanel_page.html',context)

    else: return redirect('/')


def userpanel_register_page(request):
    if not request.user.is_authenticated:

        site_settings = SiteSettings.objects.last()
        title = site_settings.site_name + " - " + "ورود کاربران"
        context = {
            'title': title,
        }
        if request.method == "POST":
            phone = str(request.POST['phone'])
            if phone.isdigit() and len(phone) == 11:
                user = Userperson.objects.filter(phone=phone).first()
                if user is not None:
                    code_check = Codes.objects.filter(user=user,status=False).count()
                    if code_check == 6:
                        return redirect('ContactUs:contactus_page')
                    else:
                        code = randint(10000,50000)
                        save_code = Codes.objects.create(user=user,code=code).save()
                        send_sms(phone,f' کد تایید شما : {code}')
                        return redirect('UserPanel:code_authentication_page',phone=phone)
                else:
                    messages.error(request,'لطفا شماره تلفن را درست وارد کنید')
                    return render(request, 'UserPanel/userpanel_login_page/userpanel_login_page.html',context)
            else:
                messages.error(request,'لطفا شماره تلفن را درست وارد کنید')
                return render(request, 'UserPanel/userpanel_login_page/userpanel_login_page.html',context)



        return render(request,'UserPanel/userpanel_login_page/userpanel_login_page.html',context)

    return redirect('/')


def userpanel_login_page(request):
    if not request.user.is_authenticated:

        site_settings = SiteSettings.objects.last()
        title = site_settings.site_name + " - " + "ورود کاربران"
        context = {
            'title': title,
        }
        if request.method == "POST":
            phone = str(request.POST['phone'])
            if phone.isdigit() and len(phone) == 11:
                user = Userperson.objects.filter(phone=phone).first()
                if user is not None:
                    code_check = Codes.objects.filter(user=user,status=False).count()
                    if code_check == 6:
                        return redirect('ContactUs:contactus_page')
                    else:
                        code = randint(10000,50000)
                        save_code = Codes.objects.create(user=user,code=code).save()
                        send_sms(phone,f' کد تایید شما : {code}')
                        return redirect('UserPanel:code_authentication_page',phone=phone)
                else:
                    messages.error(request,'لطفا شماره تلفن را درست وارد کنید')
                    return render(request, 'UserPanel/userpanel_login_page/userpanel_login_page.html',context)
            else:
                messages.error(request,'لطفا شماره تلفن را درست وارد کنید')
                return render(request, 'UserPanel/userpanel_login_page/userpanel_login_page.html',context)



        return render(request,'UserPanel/userpanel_login_page/userpanel_login_page.html',context)

    return redirect('/')





def userpanel_logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else: return redirect('UserPanel:userpanel_login_page')



def code_authentication_page(request,phone):
    if not request.user.is_authenticated:

        site_settings = SiteSettings.objects.last()
        title = site_settings.site_name + " - " + "احراز هویت کاربر"
        context = {
            'title': title,
        }

        if request.method == "POST":
            code = request.POST['code']
            user = Userperson.objects.filter(phone=phone).first()
            code_check = Codes.objects.filter(code=code,user=user,status=False).first()
            if code_check is not None:

                if user is not None:
                    codes = Codes.objects.filter(code=code,user=user,status=False).all()
                    for code in codes: codes.delete()

                    login(request, user)

                    if user.role == "user":
                        return redirect('UserPanel:userpanel_page')

                    elif user.role == 'serviceman':
                        return redirect('servicemanpanel:servicemanpanel_page')

                    elif user.is_superuser:
                        return redirect('AdminPanel:adminpanel_page')
                else:
                    return redirect('/')

            else:
                messages.error(request,'کد  تایید اشتباه است')
                return render(request,'UserPanel/code_authentication_page/code_authentication_page.html',context)

        return render(request,'UserPanel/code_authentication_page/code_authentication_page.html',context)

    else: return redirect('UserPanel:userpanel_page')