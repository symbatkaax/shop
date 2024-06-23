from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_shop.models import User
 
GROUP_CHOICES = (
    ('Покупатель', 'Покупатель'),
    ('Продавец', 'Продавец'),
)
 
ORG_TYPE_CHOICES = (
    ('ИП', 'ИП'),
    ('ООО', 'ООО'),
    ('ОАО', 'ОАО'),
    ('ЗАО', 'ЗАО'),
    ('ПАО', 'ПАО'),
)
class AuthForm(forms.Form):
    email = forms.CharField(max_length=50, label='Email адрес')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    captcha = CaptchaField(label='Captcha')
 
 
class RegistrationForm(UserCreationForm):
    group = forms.ChoiceField(choices=GROUP_CHOICES, label='Зарегистрироваться как')
    name = forms.CharField(max_length=40, label='Имя пользователя')
    surname = forms.CharField(max_length=50, label='Фамилия пользователя')
    email = forms.EmailField(label='Email адрес')
    birth_date = forms.DateField(required=False, label='Дата рождения')
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Введите пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Повторите пароль')
    captcha = CaptchaField(label='Captcha')
 
    class Meta:
        model = User
        fields = ('group', 'name', 'surname', 'email', 'birth_date', 'password1', 'password2')
 
 
class AddSellerForm(forms.Form):
    type = forms.ChoiceField(choices=ORG_TYPE_CHOICES, label='Тип организации')
    INN = forms.DecimalField(label='ИНН', max_digits=12, decimal_places=0)
    reg_date = forms.DateField(label='Дата регистрации организации')
    legal_name = forms.CharField(max_length=50, label='Юридическое название')
    email = forms.EmailField(max_length=50, label='Электронный адрес организации')
    index = forms.IntegerField(label='Почтовый индекс')
    city = forms.CharField(max_length=50, label='Город')
    street = forms.CharField(max_length=70, label='Улица')
    house_number = forms.CharField(max_length=10, label='Дом')
