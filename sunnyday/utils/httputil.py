"""JSON helper functions"""
try:
	import simplejson as json
except ImportError:
	import json

from django.http import HttpResponse

def JsonResponse(data,dump=True,status=200):
	return HttpResponse(json.dumps(data) if dump else data,content_type='application/json',status = status,)

def JsonSuccess(data):
	return JsonResponse({'data':data,'code':0})

def JsonError(error_string,status=200):
	data ={'code':1,'msg':error_string,}
	return JsonResponse(data)
JSONResponse = JsonResponse
JSONError = JsonError


