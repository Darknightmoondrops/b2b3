from CustomizedUserModel.models import Userperson


def is_user(request):
    if not request.user.is_anonymous:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user is not None:
            if user.role == 'user':
                return True
            else: return False
        else: return False

    else: return False


def is_seller(request):
    if not request.user.is_anonymous:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user is not None:
            if user.role == 'seller':
                return True
            else: return False
        else: return False

    else: return False


def is_serviceman(request):
    if not request.user.is_anonymous:
        user = Userperson.objects.filter(id=request.user.id).first()
        if user is not None:
            if user.role == 'serviceman':
                return True
            else: return False
        else: return False

    else: return False