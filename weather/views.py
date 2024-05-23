import os
import requests

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from weather_app.settings.common import DEFAULT_FROM_EMAIL


from weather import forms

from weather.models import City
from .token import account_activation_token

DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_FROM')


API_KEY = os.getenv('API_KEY')


# def user(self):
#     user_obj = User.objects.get()
#     return user_obj.email


# to_email = user()

def activate(request, uidb64, token):
    return redirect('weather')


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account'
    message = render_to_string('weather/password_reset_email.txt', {
        'user': user.username,
        'domain': get_current_site(request).domain, 'uid': urlsafe_base64_encode(
            force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure else 'http'})
    # email = EmailMessage(mail_subject, message, to=[to_email])
    # if email.send():
    #     messages.success(request, f"Dear <b>{user}</b>, please go to the \
    #                  email <b>{to_email}</b> inbox and \
    #                     click on received activation link to \
    #                         confirm and complete the registration. <b>Note</b> Check your spam folder.")
    # else:
    #     messages.error(request, f'Problem sending mail to {
    #                    to_email}, check if you typed the email address correctly')
    recipient_list = [to_email]
    # from_email = settings.DEFAULT_FROM_EMAIL  
    from_email = DEFAULT_FROM_EMAIL  


    try:
        send_mail(
            mail_subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
        messages.success(request, f"Dear <b>{user}</b>, please go to the email <b>{
                         to_email}</b> inbox and click on the received activation link to confirm and complete the registration. <b>Note</b> Check your spam folder.")
    except Exception as e:
        messages.error(request, f'Problem sending mail to {
                       to_email}, check if you typed the email address correctly. Error: {str(e)}')


def index(request):
    return redirect('weather')


def about(request):
    return render(request, 'weather/about.html')


def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))

            return redirect('weather')
    else:
        form = forms.UserRegistrationForm()
    return render(request, 'weather/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = forms.UserLoginForm()
    return render(request, 'weather/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def add_city(request):
    if request.method == 'POST':
        form = forms.CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weather')
    else:
        form = forms.CityForm()
    return render(request, 'weather/add_city.html', {'form': form})


def get_weather_data(city):
    api_key = API_KEY
    url = (
        f'http://api.openweathermap.org/data/2.5/weather?q={city}'
        f'&appid={api_key}&units=metric'
    )

    response = requests.get(url)
    return response.json()


def create_weather(request):
    city = request.GET.get('city', 'London')
    weather_data = get_weather_data(city)
    context = {
        'weather_data': weather_data,
        'city': city
    }
    return render(request, 'weather/create_weather.html', context)


def weather(request):
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        data = get_weather_data(city.name)
        weather_data.append(data)

    return render(request, 'weather/weather.html', {'weather_data': weather_data})


def city_list(request):
    cities = City.objects.all()
    weather_data_list = []

    for city in cities:
        weather_data = get_weather_data(city.name)
        if weather_data:
            weather_data_list.append(
                {'city': city.name, 'weather_data': weather_data})

    context = {'weather_data_list': weather_data_list}
    return render(request, 'weather/weather_list.html', context)


# /////////////////////


# def password_reset_request(request):
#     if request.method == "POST":
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             email = password_reset_form.cleaned_data['email']
#             user = get_object_or_404(User, email=email)
#             site = get_current_site(request)
#             subject = "Password Reset Requested"
#             email_template_name = "weather/password_reset_email.txt"
#             context = {
#                 "email": email,
#                 'domain': site.domain,
#                 'site_name': site.name,
#                 "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                 "user": user,
#                 'token': default_token_generator.make_token(user),
#                 'protocol': 'http',
#             }
#             email_content = render_to_string(email_template_name, context)
#             try:
#                 send_mail(subject, email_content, settings.EMAIL_HOST_USER, [
#                           email], fail_silently=False)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             except ConnectionRefusedError:
#                 messages.error(
#                     request, 'An error occurred while sending the password reset email. Please try again later.')
#                 return redirect("password_reset")
#             messages.success(
#                 request, 'An email with instructions to reset your password has been sent.')
#             return redirect("password_reset_done")
#     else:
#         password_reset_form = PasswordResetForm()
#     return render(request, "weather/password_reset.html", {"password_reset_form": password_reset_form})


# def reset_password(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         if request.method == 'POST':
#             password = request.POST.get('password')
#             user.set_password(password)
#             user.save()
#             messages.success(
#                 request, 'Your password has been reset successfully. You can now log in with your new password.')
#             return redirect('login')
#         return render(request, 'weather/reset_password.html')
#     else:
#         messages.error(
#             request, 'Invalid reset link. Please try again or request a new reset link.')
#         return redirect('login')
