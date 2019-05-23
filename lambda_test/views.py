from django.shortcuts import render
import http.client

# Create your views here.
def index(request):
	urlStr = 'l85qj2flnh.execute-api.us-east-1.amazonaws.com/default/my-function?key1=value1'
	conn = http.client.HTTPSConnection(urlStr)
	conn.putrequest('GET', '/')
	response = conn.getresponse()  
	print(response.read())