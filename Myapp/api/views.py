from django.shortcuts import render
from django.template.context import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponse


def email(request):
	'''
	Renders the email template
	'''
	return render(request, 'email.html')


def send_email(request):
	'''
	Sends email
	'''
	email_to = request.POST.get('to')
	email_from = request.POST.get('from')
	message = request.POST.get('message', '')
	subject = request.POST.get('subject', '')

	if subject and message and email_from:
	    try:
	        send_mail(subject, message, email_from, [email_to])
	    except BadHeaderError:
	        return HttpResponse('Invalid header found.')
	    return HttpResponseRedirect('/api/home/')
	else:
	    return HttpResponse('Make sure all fields are entered and valid.')
	


