from website.models import *


def addDefaultTemplateInformation(context):	
	# get company
	company = Company.objects.filter(active=True)
	services = Service.objects.all()
	job_categories = JobCategory.objects.all()
	jobs = Job.objects.filter(show=True)
	team_members = TeamMember.objects.all()


	# add to template
	context = {
		'company': company[0],
		'services': services,
		'categories': job_categories,
		'jobs': jobs,
		'team': team_members
	}
	
	# return context with defaults
	return context