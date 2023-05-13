from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import logout, login, authenticate
# from .decorators import *

# from .filters import PostFilter

from .models import *


# Create your views here.


def home(request):

    return render(request, 'index.html', )


def posts(request):


    return render(request, 'posts.html', )


def post(request):

    return render(request, 'post.html', )


def profile(request):
    return render(request, 'profile.html')


def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
            })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['vishwakarmaajay776@gmail.com']
            )

        email.fail_silently=True
        email.send()

    return render(request, 'email_sent.html')
