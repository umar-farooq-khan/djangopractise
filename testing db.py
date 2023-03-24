from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import pyrebase
from time import sleep
from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage

config = {
  'apiKey': "AIzaSyArHFLsk0pevFNMMGjVavppb5wltduzggw",
  'authDomain': "job-portal-c65be.firebaseapp.com",
  'projectId': "job-portal-c65be",
  'storageBucket': "job-portal-c65be.appspot.com",
  'messagingSenderId': "839506484975",
  'appId': "1:839506484975:web:a703ed5cef40c22f93451a",
  'measurementId': "G-584JGPMYSY",
'databaseURL': "https://job-portal-c65be-default-rtdb.europe-west1.firebasedatabase.app/",
}

firebase= pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()
#.order_by_child('title').equal_to('Data Scientist')
#db.child("Jobs").child("Job Detail").order_by_child("Req/title").end_at( "Data\uf8ff").get().val()
x=db.child("Jobs").child("Job Detail").child().order_by_child('id').get().val()
x

