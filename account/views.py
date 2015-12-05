from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoinForm


def user_login(request):
    if request.method == 'POST':
        form = LoinForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Auth successfully')
                else:
                    return HttpResponse('DISABLED')
            else:
                return HttpResponse('invalid login')
    else:
        form = LoinForm()
    return render(request, 'account/login.html', {'form': form})


