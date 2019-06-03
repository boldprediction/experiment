from django.shortcuts import render
import http.client
import requests

# Create your views here.
def index(request):
	ulr_str = 'https://l85qj2flnh.execute-api.us-east-1.amazonaws.com/default/my-function?key1=value1'
	response = requests.get(ulr_str)
	# conn = http.client.HTTPSConnection(urlStr)
	# conn.putrequest('GET', '/')
	# response = conn.getresponse()  
	print(response.content)
	return render(request, 'lambda_test/index.html', {})

