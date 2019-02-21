from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))] #
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

class LoginMiddleware:

	def __init__(self,get_response):
		self.get_response=get_response

	def __call__(self,request):
		print("Hello -----------------")
		print(EXEMPT_URLS)
		response= self.get_response(request)

		return response
	def processrequest(self,request):
		print("&&&&&&&&&&&&&&&&&&&&&")
		assert hasattr(request, 'user')
		print("**************************")
		print(request)
		if not request.user.is_authenticated():
			path = request.path_info.lstrip('/') #
			print(path)
			if not any(m.match(path) for m in EXEMPT_URLS):

			    return HttpResponseRedirect(settings.LOGIN_URL)



# import re
# from django.conf import settings 
# from django.shortcuts import redirect 
# print(settings.LOGIN_URL)
# EXEMPT_URLS=[re.compile(settings.LOGIN_URL.lstrip('/'))] #

# if hasattr(settings,'LOGIN_EXEMPT_URL'):
# 	EXEMPT_URLS +=[re.compile(url) for url in settings.LOGIN_EXEMPT_URL]

# class LoginMiddleware:
# 	def __init__(self,get_response):
# 		self.get_response=get_response

# 	def __call__(self,request):
# 		print("Hello -----------------")
# 		response= self.get_response(request)

# 		return response

# 	def process_view(self, request, view_func, *view_args, **view_kwargs):
# 		print(request)		