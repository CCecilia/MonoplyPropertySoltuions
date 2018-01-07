__author__ = 'christian.cecilia1@gmail.com'
from django.http import JsonResponse
from django.shortcuts import render
import smtplib
from .models import *


def index(request):
	# dec vars
	services = Service.objects.all()
	job_categories = JobCategory.objects.all()
	jobs = Job.objects.filter(show=True)
	team_members = TeamMember.objects.filter(show=True)

	context = {
		'services': services,
		'categories': job_categories,
		'jobs': jobs,
		'team': team_members
	}

	return render(request, 'index.html', context)

def contactFormSend(request):
	name = request.POST['name']
	subject = request.POST['subject']
	email = request.POST['email']
	message = request.POST['message']
	company = Company.objects.filter(active=True)

	print(name, subject, email, message)

	try:
		# set up email header/message
		header = 'Subject:{}\n\nFrom:{}\n'.format(subject, email)
		message = header + message

		# smtp
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		# login smtp
		server.login(company[0].email_username, company[0].email_password)
		# send email
		server.sendmail(email, [company[0].email], message)
		# close server
		server.quit()

		# create response
		response = {
			'status': 200
		}
	except IndexError:
		# create response
		response = {
			'status': 500,
			'error_message': 'comapny email not set up'
		}

	# send reponse JSON
	return JsonResponse(response)
