from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password


User = get_user_model()



class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True, label='Имя пользователя', widget=forms.TextInput(attrs={
        'id':  'sign-email',
        'class': 'sign__input',
        'placeholder': 'Email или ваша почта'
    }))

    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput(attrs={
        'id': 'sign-password',
        'class': 'sign__input',
        'placeholder': 'Пароль'
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Email не найден попробуйте снова')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')

            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Данный пользователь не активен')
        return super().clean(*args, **kwargs)


class RegistrationForm(forms.ModelForm):

    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'sign__input required',
        'placeholder': 'Email или ваша почта',
        'id': 'reg-email',
        'name': 'reg-email',
        'type': 'text'
    }))

    password = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'sign__input required',
        'placeholder': 'Пароль',
        'id': 'reg-password',
        'name': 'reg-password',
        'type': 'password'
    }))

    password2 = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'sign__input required',
        'placeholder': 'Повторите пароль',
        'id': 'reg-repeat-password',
        'name': 'reg-password',
        'type': 'password'
    }))

    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'name',
        'name': 'name',
        'class': 'sign__input required',
        'placeholder': 'Например Айбек'
    }))

    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'surname',
        'name': 'surname',
        'class': 'sign__input required',
        'placeholder': 'Ваша Фамилия'
    }))

    patronymic = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'patronymic',
        'name': 'patronymic',
        'class': 'sign__input',
        'placeholder': 'Ваше Отчество'
    }))

    phone = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'phone',
        'name': 'phone',
        'class': 'sign__input',
        'placeholder': 'Ваше номер телефона'
    }))

    telegram = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'telegrambot',
        'name': 'telegrambot',
        'class': 'sign__input',
        'placeholder': '@Nickname'
    }))

    city = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'city',
        'name': 'city',
        'class': 'sign__input required',
        'placeholder': 'Ваш город'
    }))

    address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'address',
        'name': 'address',
        'class': 'sign__input required',
        'placeholder': 'Адрес фактического проживания'
    }))

    apartment = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'type': 'text',
        'id': 'apartment',
        'name': 'apartment',
        'class': 'sign__input required',
        'placeholder': 'Например Третий'
    }))

    postcode = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'id': 'postcode',
        'name': 'postcode',
        'class': 'sign__input required',
        'placeholder': 'Например Третий'
    }))

    scan_out = forms.ImageField(required=True, widget=forms.FileInput(attrs={
        'type': 'file',
        'id': 'scan-out',
        'name': '',
        'accept': 'image/*'
    }))

    scan_in = forms.ImageField(required=True, widget=forms.FileInput(attrs={
        'type': 'file',
        'id': 'scan-in',
        'name': '',
        'accept': 'image/*'
    }))

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'patronymic', 'phone', 'telegram',
                  'city', 'address', 'apartment', 'scan_out', 'scan_in']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']


class EmailForm(forms.Form):
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'id': 'forget-password-email',
        'class': 'sign__input',
        'placeholder': "Primer@gmail.com",
        'type': "text",
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Email не найден попробуйте снова')
            if not email:
                raise forms.ValidationError('Данный пользователь не активен')
        return super().clean(*args, **kwargs)


class ResetForm(forms.Form):

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'id': 'sign-password',
        'class': 'sign__input',
        'placeholder': 'Ваш новый пароль'
    }))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'id': 'sign-password',
        'class': 'sign__input',
        'placeholder': 'Повторите новый пароль'
    }))

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']