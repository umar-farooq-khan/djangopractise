
#import pyrebase
#import  json
#import pandas as pd

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


df=pd.read_csv(r'output_file_all_countries.csv')
df
df=df[df['Country']== 'Sweden']

df= df.drop(['op_desc'], axis=1)

def extract_link(link):
    return link.split('/openings/')[-1]

# Apply the function to the 'links' column and store the result in a new column
df['poster_link'] = df['op_link_'].apply(extract_link)


df= df.drop(['op_link_'], axis=1)

df.to_csv('preprocessed_jobs_nexer.csv')


df
df.read_csv(r'preprocessed_jobs_nexer')
df.columns
#!!!!!!!!!!!delete unnamed cols !!!!!!!!!!!!!!!!!remember it!!!!!!!!







json_data = df.to_json(orient='records')
# Print the JSON data


job_list = json.loads(json_data)
for i in range(0 , len(job_list)):
    job_list[i]['title']=job_list[i]['title'].upper()

#drop any unnamed columns !!!!!!!!!!!remeber it plessss!!!!
for i in range(0 , len(job_list)):
    db.child('Jobs').child('Job Detail').child(job_list[i]['id']).child('Req').set(job_list[i])





parent_node = "Jobs/Job Detail"

# Get a reference to the parent node
parent_node_ref = db.child(parent_node)
child_nodes = parent_node_ref.get().val()



# Loop through each child node and delete the specified fields
for child_node_key in child_nodes:
    child_node_ref = parent_node_ref.child(child_node_key)
    print(child_node_ref)
    child_node_ref.update({"Unnamed: 10": None, "op_desc": None})

print("Fields deleted successfully!")