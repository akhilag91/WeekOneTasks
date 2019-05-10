from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

@shared_task
def sendmail(subject,from_email, to_email):
    html_content = render_to_string('Todo.html', {'subject' : subject})
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print("In celery")
        