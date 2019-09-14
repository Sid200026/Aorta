from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
import numpy as np
import pickle
import os

# Create your views here.

@login_required
def predict(request):
	if request.method == 'GET':
		if request.user.user_type == 'Patient':
			return render(request,'predict/index.html')
		else:
			# return HttpResponseRedirect(reverse('mainapp:reguser'))
			return HttpResponse('not patient')
	if request.method == 'POST':
		if request.user.user_type == 'Patient':
			with open('predict/model.pkl','rb') as model_pkl:
				model = pickle.load(model_pkl)
				request_values=request.POST
				request_values=request_values.dict()
				del request_values['csrfmiddlewaretoken']
				int_features = [int(x) for x in request_values.values()]
				final_features = [np.array(int_features)]
				final_features=np.int64(final_features)
				prediction = model.predict(final_features)
				output = round(prediction[0], 2)
				if(output == 1):
					message="You might have a condition, consult a doctor"
				else:
					message="Your heart is healthy"
				return render(request,'predict/results.html',{'output':message})
		else:
			# return HttpResponseRedirect(reverse('mainapp:reguser'))
			return HttpResponse('not patient')

