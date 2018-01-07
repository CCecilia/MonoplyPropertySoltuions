from website.models import *


def addDefaultTemplateInformation(context):
	# get company
	company = Company.objects.filter(active=True)

	# add to template
	context = {
		'company': company[0]
	}
	
	# return context with defaults
	return context
