
import pyrebase

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
# Initialize the Firebase Storage client
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()
storage = firebase.storage()


import pandas as pd

df=pd.read_csv(r'nexer_jobs.csv')
import  json

json_data = df.to_json(orient='records')
# Print the JSON data
job_list = json.loads(json_data)
for i in range(0 , len(job_list)):
    job_list[i]['title']=job_list[i]['title'].upper()

print(job_list)
for i in range(0 , len(job_list)):

    db.child('Jobs').child('Job Detail').child(job_list[i]['id']).child('Req').set(job_list[i])




