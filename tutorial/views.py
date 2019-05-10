# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from mytutorial import settings

from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string
from tutorial.tasks import sendmail

""" sending text messages """

def email(request):
    if request.method == 'GET':
        return render(request,'home.html')
    elif request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        to_email = request.POST.get('to_email', '')
        
        if subject and message and to_email:
            try:
                send_mail(subject, message,'Akhila', [ to_email ])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('success')
        else:

            return HttpResponse('Make sure all fields are entered and valid.')  

"""using templates to send email"""

def sendemail(request):
    if request.method == "GET":
        return render(request,'home.html')
    elif request.method  == "POST":
        subject = request.POST.get('subject', '')
        to_email = request.POST.get('to_email', '')
        from_email =  'akhila<akhila@tapchief.com>'
        sendmail.delay(subject=subject, from_email=from_email, to_email=to_email)
        return HttpResponse('success')





