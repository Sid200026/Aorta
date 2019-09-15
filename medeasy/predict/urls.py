from django.urls import path
from . import views

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app_name='predict'

urlpatterns=[
	path('predict/', views.predict, name="predicter"),
	path('predict/save',views.saveresults,name="saveresult")
]