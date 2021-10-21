from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegistrationForm, LoginForm, EmailForm, ResetForm

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('pages/sign.html')
            
        return render(request, 'pages/registration.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'pages/registration.html', {'form': form})


def login_view(request):

    _next = request.GET.get('next')  # MAIN
    form = LoginForm()
    email_form = EmailForm()

    if request.method == 'POST' and 'login' in request.POST:

        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            login(request, user)
            _next = _next or '/'
            return redirect(_next)

        return render(request, 'pages/sign.html', {'form': form, 'email_form': email_form})

    return render(request, 'pages/sign.html', {'form': form, 'email_form': email_form})


def forget_email(request):

    if request.method == 'POST':
        email = list(dict(request.POST).get('email'))[0]
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            pk = user.id
            token = user.password
            token = token.replace('/','')
            url = f'{request.get_host()}{reverse("reset",args=[pk, token])}'
            send_mail("Изменение пароля", f'Чтобы изменить пароль, перейдите по ссылке: http://{url}',
                      'qubanu4.s@gmail.com', [email], fail_silently=False)

            return HttpResponse('Мы отправили на почту')

        else:

            return HttpResponse('Такого пользователя нет')

    return HttpResponse('GET')


def reset(request, pk, token):

    user = User.objects.get(id=pk)
    token_db = user.password.replace('/','')
    form = ResetForm()

    if token_db == token and request.method == 'GET':
        return render(request, 'pages/reset.html', {'form': form})

    if request.method == 'POST':
        form = ResetForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

        return HttpResponseRedirect(reverse('login'))
    return HttpResponse('Такого адреса не существует')


def logout_view(request):
    logout(request)
    return redirect('/')



