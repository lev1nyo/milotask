from random import randint
from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import UserNew


def user_list(request):
    context = {
        'users': UserNew.objects.all()
    }
    return render(request, 'list.html', context)


def user_view(request, user_id):
    context = {
        'user': UserNew.objects.get(pk=user_id)
    }
    return render(request, 'view.html', context)


def user_edit(request, user_id):
    try:
        user = UserNew.objects.get(pk=user_id)
    except UserNew.DoesNotExist:
        random_number = randint(1, 100)
        user = UserNew(
            random_number=random_number,
            username='New User ' + str(random_number),
            birthday=datetime.now()
        )
        user.save()
        return HttpResponseRedirect('/user/')

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.birthday = request.POST.get('birthdate')
        user.save()
        return HttpResponseRedirect('/user/')

    else:
        context = {'user': user}

    return render(request, 'edit.html', context)


def user_delete(request, user_id):
    try:
        user = UserNew.objects.get(pk=user_id)
        user.delete()

    except UserNew.DoesNotExist:
        pass

    return HttpResponseRedirect('/user/')
