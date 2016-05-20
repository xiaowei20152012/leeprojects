# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,Http404

from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.views.decorators.csrf import csrf_exempt

from sunuser.models import User
from sunuser.dbmodels import Blog,Author,Entry
from utils.dictutils import to_dict,get_sign,createToken
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
		if user.verify_password(password):
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

@csrf_exempt
def getNews(request):
	try:
#		entry = Blog.objects.filter(entry__headline__contains='top')
		entry = Entry.objects.filter(blog__name__exact='xiaowei hao 1')
		return HttpResponse(entry)
	except Exception, e:
		print e
		entry = None
		return JsonError("hello")
	else:
		entry = None
		return JsonError("hello1")

@csrf_exempt
def getUser(request):
	if request.method != 'POST':
		raise Http404(error404)
	appnum = request.POST.get('appnum')
	battery = request.POST.get('battery')
	channelid = request.POST.get('channelid')
	deviceid = request.POST.get('deviceid')
	factory = request.POST.get('factory')
	imsi = request.POST.get('imsi')
	oscode = request.POST.get('oscode')
	phoneModel = request.POST.get('phoneModel')
	platform = request.POST.get('platform')
	productid = request.POST.get('productid')
	resolution = request.POST.get('resolution')
	sd = request.POST.get('sd')
	isp = request.POST.get('isp')
	uuid = request.POST.get('uuid')
	sign = request.POST.get('sign')
	dict_user ={}
	dict_user['appnum'] = appnum
	dict_user['battery'] = battery
	dict_user['channelid'] = channelid
	dict_user['platform'] =platform
	dict_user['productid'] = productid
	dict_user['resolution'] = resolution
	dict_user['sd'] = sd
	dict_user['isp'] = isp
	dict_user['uuid'] = uuid
	dict_user['deviceid'] = deviceid
	dict_user['factory'] = factory
	dict_user['imsi'] = imsi
	dict_user['oscode'] = oscode
	dict_user['phoneModel'] = phoneModel

	if str(get_sign(dict_user)) == sign:
		return HttpResponse(u'签名认证通过')
	else:
		return HttpResponse(u'签名认证失败')
#	return HttpResponse(dict_user)


@csrf_exempt
def userexmaple(request):
	if request.method != 'POST':
		raise Http404(error404)
	
	username = request.POST.get('username')
	password = request.POST.get('password')
	try:
		user = User.objects.get(username=username)
		if user.verify_password(password):
			user.login()
			return JsonSuccess(user.as_json())
		else:
			return JsonError("the password is wrong%s" % user.password)
	except:
		return JsonError("this user is not exist")
	else:
		return JsonError("there is some other problems")
	
	

	return JsonError(str(createToken('hello')))
	

def printinfo(request):

	
	return makeToken('hello')


