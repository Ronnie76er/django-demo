from django.http import HttpResponse
from django.template import Context, loader
from testapp.models import *

def index(request):
	user_list = TestUser.objects.all().order_by('-create_date')
	template = loader.get_template('testapp/index.html')
	c = Context({
		'user_list':user_list,
	})

	return HttpResponse(template.render(c))

def detail(request, user_id):
	user = TestUser.objects.get(id = user_id)
	template = loader.get_template('testapp/userinfo.html')
	c = Context({
		'user': user
		})
	return HttpResponse(template.render(c))