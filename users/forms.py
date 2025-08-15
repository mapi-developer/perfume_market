from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
          widget=forms.TextInput(attrs={"autofocus": True,
                                        "class": "form-control",
                                        "placeholder": "Введите ваше имя пользователя"})
    )
    password = forms.CharField(
          widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                            "class": "form-control",
                                            "placeholder": "Введите ваш пароль"})
    )

    class Meta:
            model = User()
            fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
      first_name = forms.CharField(
            widget=forms.TextInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите ваше имя",
                  }
            )
      )

      last_name = forms.CharField(
            widget=forms.TextInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите вашу фамилию",
                  }
            )
      )

      username = forms.CharField(
            widget=forms.TextInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите ваше имя пользователя",
                  }
            )
      )

      email = forms.CharField(
            widget=forms.EmailInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите ваш email",
                  }
            )
      )

      password1 = forms.CharField(
            widget=forms.PasswordInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите ваш пароль",
                  }
            )
      )

      password2 = forms.CharField(
            widget=forms.PasswordInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Подтвердите ваш пароль",
                  }
            )
      )

      class Meta:
            model = User
            fields = (
                  "first_name",
                  "last_name",
                  "username",
                  "email",
                  "password1",
                  "password2"
            )

class ProfileForm(UserChangeForm):
      image = forms.ImageField(
            widget=forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
      )

      first_name = forms.CharField(
            widget=forms.TextInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите ваше имя",
                  }
            )
      )

      last_name = forms.CharField(
            widget=forms.TextInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите вашу фамилию",
                  }
            )
      )

      username = forms.CharField(
            widget=forms.TextInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите ваше имя пользователя",
                  }
            )
      )

      email = forms.CharField(
            widget=forms.EmailInput(
                  attrs={
                        "class": "form-control",
                        "placeholder": "Введите ваш email",
                        "readonly": True,
                  }
            )
      )

      class Meta:
            model = User
            fields = (
                  "image",
                  "first_name",
                  "last_name",
                  "username",
                  "email",
            )