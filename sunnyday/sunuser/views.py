# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,Http404

from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.views.decorators.csrf import csrf_exempt

from sunuser.models import User
from utils.dictutils import to_dict
from utils.httputil import JsonError,JsonSuccess

# Create your views here.
error404 = 'unsupport request GET,please use POST'

def index(request):
	return HttpResponse(u"Welcome to the world");


@csrf_exempt
def register(request):
	if request.method !='POST':
		raise Http404(error404);
	username = request.POST.get('username')
	nickname = request.POST.get('nickname')
	password = request.POST.get('password')
	verifypsd = request.POST.get('verifypsd');
	if not (username and password and verifypsd):
		return JsonError('用户名密码不能为空')
	if password != verifypsd:
		return JsonError('两次密码输入不一致')
	try :
		user = User.objects.get(username = username)
	except ObjectDoesNotExist:
		user = None
	except Exception:
		user = None
	if user:
		return JsonError('用户已存在')
	else:
		user = User()
		user.username = username
		user.nickname = nickname
		user.set_password(password)
		user.save_user()
		user.login()

	return JsonSuccess(to_dict(user))

@csrf_exempt
def login(request):
	if request.method != 'POST':
		raise Http404(error404)
	username = request.POST.get('username')
	password = request.POST.get('password')
	try:
		user = User.objects.get(username=username)
		if not user.verify_password(password):
			user.login()
			return JsonSuccess(user.as_json())
		else:
			return JsonError("the password is wrong%s" % user.password)
	except:
		return JsonError("this user is not exist")
	else:
		return JsonError("there is some other problems")
	
@csrf_exempt
def  forget(request):
	if request.method != 'POST':
		raise Http404(error404)
	username = request.POST.get('username')
	nickname = request.POST.get('nickname')
	repsd = request.POST.get('repassword')
	try:
		user = User.objects.get(username=username,nickname=nickname)
		user.set_password(repsd)
		user.save_user()
		user.login()
		return JsonSuccess(user.as_json())
	except:
		return JsonError("the user is not exist")
	else:
		return HttpResponse(u'forget')
