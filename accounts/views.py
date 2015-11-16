# -*- coding: utf-8 -*-e 
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        args['username'] = auth.get_user(request).username
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return redirect("/")
        else:
            # todo сделать ошибку ввода пароля
            args['login_error'] = "Не правильный логин или пароль!"
            # Отображение страницы с ошибкой
            return render_to_response("login.html", args)
    else:
        return render_to_response("login.html", args)


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return redirect("/accounts/login/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect("/testing/")
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)
