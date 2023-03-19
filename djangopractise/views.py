from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import pyrebase
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from firebase_admin import storage
from collections import OrderedDict
import spacy
import ocrspace
from django.views.decorators.csrf import csrf_protect
from time import sleep
from django.core.mail import send_mail
import django.utils.datastructures as imp
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.urls import reverse

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


def home(request):
    # jobdic_orig=db.child('Jobs').child('Job Detail').get().val()
    jobdic = OrderedDict([('1001', {'Applicants': {
        'abubakarkhan99': {'coverletter_name': ' ctvgnjmkmjnhbvfcdxsxdgfvhnjmk,l',
                           'email_name': 'abubakar_khan_99@hotmail.com', 'eu_eligible_name': 'y', 'exp_name': '2',
                           'firstname_name': 'Hafiz', 'lastname_name': 'Khan', 'phonenum_name': '+46735625456',
                           'url_cv': 'https://firebasestorage.googleapis.com/v0/b/job-portal-c65be.appspot.com/o/files%2FInternational%20Deferral%20Form%20-%20NCIRL.pdf?alt=media'},
        'umarkhan2840503': {'coverletter_name': ' ghjlk', 'email_name': 'umarkhan2840503@gmail.com',
                            'eu_eligible_name': '', 'exp_name': '', 'firstname_name': 'Umar', 'lastname_name': 'Khan',
                            'phonenum_name': '+923365297082',
                            'url_cv': 'https://firebasestorage.googleapis.com/v0/b/job-portal-c65be.appspot.com/o/files%2FUmar%20Farooq%20Khan%20CV.pdf?alt=media'}},
                                    'Req': {'company': 'Facebook', 'deadline': '01/03/2023',
                                            'desc': '<div class="job-text">     <h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Personality / Commitment</h2><p>At Jobba in Gothenburg, Sweden we work with some of Sweden’s largest automotive manufacturers within research and development. Now we are looking to expand our team of automotive software test engineers. Within the field of testing, the trend is moving towards automation. Therefore, we are looking for you who are an automotive software test engineer or automotive software developer, preferably experienced with Python and Continuous Integration (CI/CD). Here, we encourage and support our engineers to evolve professionally as personally. Therefore, you will have the fullest support from your closest Jobba manager, who will follow you in your journey and support you forward – in the direction you want. When you feel like you want to learn something new, you can always take it into your own hands because Jobba Academy offers several educations, from new programming languages to negotiation skills and much more.</p><h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Job / Skills</h2><p>To be successful in this role, we believe that you have:</p> <ul><li>Minimum 5 years of experience working with automotive software, either testing or development.</li> <li>Professional experience working with Python or C++.</li> <li>Worked in an Agile environment.</li> <li>A relevant degree in Computer Science, Software Engineering, Electronics, Data Science, Mathematics, Physics or similar.</li> </ul><p>Meritorious experience:</p> <ul><li>Experience in PyTest or Robot Framework.</li> <li>Experience with CI/CD tools e.g. Jenkins.</li> <li>Experience with Vector tools e.g. CANoe, CANalyzer.</li> <li>Experience with CAN, LIN, Ethernet.</li> </ul><p>&nbsp;To succeed in the role as a consultant at Jobba you need to be analytical, have a great sense for quality, a positive attitude and you need to be a team-player. If You find this as an interesting next step and would like to get in touch with us, don’t hesitate to send in your application.&nbsp;</p> <p><strong>About JOBBA</strong></p> <p>Jobba is one of Europe’s largest technology and IT consulting companies with over 45,000 employees in over 30 countries. Our engineers carry out complex and highly technical projects throughout the value chain of the most prestigious companies in all sectors, such as Automotive, Telecom, Industry, Energy, Aerospace &amp; Defense and Life Science. In Sweden, we are over 1300 committed employees with 11 offices in 10 cities - from Lund in the south to Skellefteå in the north.</p> <p>For the fourth year in a row, Jobba has been named one of Sweden\'s most attractive employers by Karriärföretagen 2023, an award for employers that offer unique career and development opportunities.</p> <p>Welcome to read more about us at&nbsp;<a href="#" target="_blank" rel="noreferrer noopener">jobba.se</a></p> <p>We are looking forward to your application!</p>    </div>',
                                            'experience': '3+', 'expiry': '20/10/2023', 'id': '1001',
                                            'loc': 'Menlo Park', 'location': 'Jonkoping', 'postdate': '08/01/2019',
                                            'salary': '110000', 'title': 'Data Scientist', 'type': 'Full time'}}), (
                          '1002', {'Applicants': {
                              'abubakarkhan99': {'coverletter_name': ' sdfhj,kl.ukyuyhrsrfwergtshyjufyjh',
                                                 'email_name': 'abubakar_khan_99@hotmail.com',
                                                 'eu_eligible_name': 'yes', 'exp_name': '2', 'firstname_name': 'Hafiz',
                                                 'lastname_name': 'Khan', 'phonenum_name': '+46735625456',
                                                 'url_cv': 'https://firebasestorage.googleapis.com/v0/b/job-portal-c65be.appspot.com/o/files%2FInternational%20Deferral%20Form%20-%20NCIRL.pdf?alt=media'}},
                                   'Req': {'company': 'Amazon', 'deadline': '01/03/2023',
                                           'desc': '<div class="job-text">     <h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Personality / Commitment</h2><p><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">To fit into this role, you need to have a personality that exudes drive and proactivity. </font><font style="vertical-align: inherit;">You are a problem-solving oriented and positive person who enjoys working in teams to jointly reach the best solution.</font></font><br> &nbsp;</span></p><h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Job / Skills</h2><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Now we have an opportunity for you who want to work in manufacturing. </font><font style="vertical-align: inherit;">The role is within production technology with a focus on PLC programming. </font><font style="vertical-align: inherit;">We are now looking for automation engineers with education or experience.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">As a consultant with us, you work with the main focus on PLC programming for one of our clients. </font><font style="vertical-align: inherit;">Furthermore, you get both a team feeling in your assignment and a really lovely community at ALTEN. </font><font style="vertical-align: inherit;">Through our internal networks ALTEN Sports, Women@ALTEN and ALTEN Innovation, you are given the opportunity to pursue issues and activities that you are passionate about, together with your colleagues. </font><font style="vertical-align: inherit;">Everything is of course voluntary. </font><font style="vertical-align: inherit;">We place balance between work and private life at the top of the list. </font><font style="vertical-align: inherit;">Of course, we have a collective agreement. </font><font style="vertical-align: inherit;">In addition to this, we have benefits such as health care allowance, occupational pension and insurance.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">We are looking for you as a manufacturing engineer as you join as a production technician with a focus on automation. </font><font style="vertical-align: inherit;">Together with other technicians in the area, you will drive technology development to reach the goals set for the area in the form of technical availability, production cost, ergonomics, volume and quality. </font><font style="vertical-align: inherit;">The role requires a genuine interest in technology, analytical ability and collaborative skills. </font><font style="vertical-align: inherit;">In the role, you have to manage stakeholders in the form of operators, production managers, PT colleagues, maintenance and suppliers.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The challenges are to drive improvement work together with other support functions at the same time in close cooperation with our customer\'s suppliers. </font><font style="vertical-align: inherit;">The service requires a technical understanding, but also an understanding to deliver the product at the right cost and quality.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Our customer has challenges regarding automation in several areas, which will also be part of the service to provide assistance and training for current employees. </font><font style="vertical-align: inherit;">Driving the technical development of automation requires technical curiosity, as well as good collaboration skills as it will always take place in consultation with several stakeholders. </font><font style="vertical-align: inherit;">This will require a great focus on getting to know the process and its parameters, as well as understanding how the process affects outcomes on the product but also subsequent processes. </font><font style="vertical-align: inherit;">Furthermore, it becomes a challenge to be in a factory during start-up, where routines are under construction, both with regard to the process itself, but also organizationally. </font><font style="vertical-align: inherit;">In other words, you must be prepared for changes to occur.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Training:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">University education in mechanical engineering/automation.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Production technical training meritorious.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Competency requirements:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">PLC programming is a requirement.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Analytical ability. </font><font style="vertical-align: inherit;">Ability to understand and break down complex problems when troubleshooting, for example. </font><font style="vertical-align: inherit;">Genuine technical interest, as this is an area of \u200b\u200brapid technological development.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Good cooperation skills with other technicians, maintenance but also understanding of operators, production managers and their requirements for delivery.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Meritorious:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge of CNC controllers and robot handling.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge in vision technology.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Experience of working within highly automated flows.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Swedish in both speech and writing.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">English in both speech and writing.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Characteristics/values</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Documented, thorough, quality conscious &amp; committed.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Good cooperation skills.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Technically interested in machines and processes.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Strong personal drive.</font></font></li> </ul><p><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">What do we offer?</font></font></strong></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Every employee is equally important in ALTEN\'s success! </font><font style="vertical-align: inherit;">We believe in growing together by offering opportunities, development and community. </font><font style="vertical-align: inherit;">ALTEN operates in several different industries, has a large variety of assignments, coaching managers and training via the ALTEN Academy, which means that it will always be possible to develop with us. </font><font style="vertical-align: inherit;">Your wishes guide your path forward. </font><font style="vertical-align: inherit;">Through our internal networks such as Women@ALTEN and ALTEN Sports, you are given the opportunity to pursue issues and activities that you are passionate about. </font><font style="vertical-align: inherit;">At ALTEN, we think it is important to have a balance between work and leisure, which is why we offer three extra days off per year. </font><font style="vertical-align: inherit;">With us, you are connected to a collective agreement and are offered benefits such as health benefits, occupational pension and insurance.</font></font></p> <p>&nbsp;<strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Om OLD</font></font></strong></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ALTEN is one of Europe\'s largest technology and IT consulting companies with over 45,000 employees in more than 30 countries. </font><font style="vertical-align: inherit;">Our engineers carry out complex and highly technical projects throughout the entire product development chain at the leading companies in several different industries such as Automotive, Telecom, Industry, Energy, Aviation and Defense as well as Life Science. </font><font style="vertical-align: inherit;">In Sweden, we are over 1,300 committed employees with 11 offices in 10 cities - from Lund in the south to Skellefteå in the north.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">For the third year in a row, ALTEN has been named one of Sweden\'s most attractive employers by Career Companies 2022, an award for employers that offer unique career and development opportunities.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Welcome to read more about us at&nbsp; </font></font><a href="https://www.alten.se/" target="_blank" rel="noreferrer noopener"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">alten.se</font></font></a></p> <p>&nbsp;</p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A warm welcome with your application!</font></font></p>    </div>',
                                           'experience': '5+', 'expiry': '20/10/2023', 'id': '1002', 'loc': 'Seattle',
                                           'postdate': '08/01/2019', 'salary': '130000',
                                           'title': 'Production Techniques - Automation', 'type': 'Full time'}}), (
                          '1003', {'Req': {'company': 'Microsoft', 'deadline': '01/03/2023',
                                           'desc': 'As an AI Engineer at Microsoft, you will work on building and deploying advanced AI and machine learning systems. You will collaborate with a team of researchers and engineers to develop cutting-edge algorithms, and implement them in real-world applications. Minimum qualifications include a bachelors degree in Computer Science, Electrical Engineering, or a related field, and 2+ years of experience in AI or machine learning.',
                                           'experience': '2+', 'expiry': '20/10/2023', 'id': '1003', 'loc': 'Redmond',
                                           'postdate': '08/01/2019', 'salary': '100000', 'title': 'AI Engineer',
                                           'type': 'Full time'}}), ('1004', {
        'Req': {'company': 'Amazon', 'deadline': '01/03/2023',
                'desc': 'The DevOps Engineer will be responsible for designing, implementing, and maintaining the infrastructure and tools to support the development and deployment of software. You will work closely with development teams to understand their needs and provide solutions to improve the overall software delivery process. The ideal candidate will have experience with cloud infrastructure, automation, and continuous integration/delivery.',
                'experience': '5+', 'expiry': '20/10/2023', 'id': '1004', 'loc': 'Seattle', 'postdate': '08/01/2019',
                'salary': '130000', 'title': 'DevOps Engineer', 'type': 'Full time'}}), ('1006', {
        'Req': {'company': 'Microsoft', 'deadline': '01/03/2023',
                'desc': 'The AI Engineer will be responsible for designing, developing and deploying AI-based solutions to improve various aspects of the Microsoft product and services. You will work closely with cross-functional teams to understand business needs, identify opportunities, and deliver data-driven solutions. The ideal candidate will have a background in computer science or a related field, and have experience in machine learning, data mining and modeling.',
                'experience': '2+', 'expiry': '20/10/2023', 'id': '1006', 'loc': 'Redmond', 'postdate': '08/01/2019',
                'salary': '100000', 'title': 'ML Engineer', 'type': 'Full time'}}), ('1007', {
        'Req': {'company': 'Apple', 'deadline': '01/03/2023',
                'desc': 'The iOS Developer will be responsible for designing, developing and testing iOS applications. You will work closely with cross-functional teams to understand business needs, identify opportunities, and deliver high-quality solutions. The ideal candidate will have a background in computer science or a related field, and have experience in iOS development, Swift and Objective-C.',
                'experience': '5+', 'expiry': '10/10/2023', 'id': '1007', 'loc': 'Redmond', 'postdate': '08/01/2019',
                'salary': '100000', 'title': 'AI Engineer', 'type': 'Full time'}})])

    print('home func ran', jobdic)
    if request.method == 'POST':
        print(request)
        a = request.POST['text_search']
        print(a)
        jobdic = db.child("Jobs").child("Job Detail").order_by_child("Req/title").start_at(a).end_at(
            a + "\uf8ff").get().val()
        # First word capital hoga Db main to agar small liko ge to search nahe karega
        print(jobdic)

    if request.method == 'POST' and 'submit_btn' in request.POST and request.POST['submit_btn'] == 'clicked':
            print('post request')
            print(request)
            context = {}
            context['hey'] = 'some string'
            return render(request, 'index.html', {
                 'job_id': context})

    if 'clicked' in request.GET:
        if request.GET['clicked'] == 'xdfd':
            # do something
            print('yahoooo called function')
            pass
    return render(request, 'index.html', {
        'data': jobdic
    })
def r_jobdetail(request):
    context = {}
    if request.method == 'POST':
        print(request)
        try:
            a = request.POST['text_search']
            print(a)
            context['data'] = db.child("Jobs").child("Job Detail").order_by_child("Req/title").start_at(a).end_at(
                a + "\uf8ff").get().val()
            # First word capital hoga Db main to agar small liko ge to search nahe karega
            print(context)
            return render(request, 'job_detail_pg.html', {
                'job_id': context})
        except imp.MultiValueDictKeyError:
            print('Mutlitplvalue erro')

    jobdic = OrderedDict([('1001', {'Applicants': {
        'abubakarkhan99': {'coverletter_name': ' ctvgnjmkmjnhbvfcdxsxdgfvhnjmk,l',
                           'email_name': 'abubakar_khan_99@hotmail.com', 'eu_eligible_name': 'y', 'exp_name': '2',
                           'firstname_name': 'Hafiz', 'lastname_name': 'Khan', 'phonenum_name': '+46735625456',
                           'url_cv': 'https://firebasestorage.googleapis.com/v0/b/job-portal-c65be.appspot.com/o/files%2FInternational%20Deferral%20Form%20-%20NCIRL.pdf?alt=media'},
        'umarkhan2840503': {'coverletter_name': ' ghjlk', 'email_name': 'umarkhan2840503@gmail.com',
                            'eu_eligible_name': '', 'exp_name': '', 'firstname_name': 'Umar', 'lastname_name': 'Khan',
                            'phonenum_name': '+923365297082',
                            'url_cv': 'https://firebasestorage.googleapis.com/v0/b/job-portal-c65be.appspot.com/o/files%2FUmar%20Farooq%20Khan%20CV.pdf?alt=media'}},
                                    'Req': {'company': 'Facebook', 'deadline': '01/03/2023',
                                            'desc': '<div class="job-text">     <h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Personality / Commitment</h2><p>At Jobba in Gothenburg, Sweden we work with some of Sweden’s largest automotive manufacturers within research and development. Now we are looking to expand our team of automotive software test engineers. Within the field of testing, the trend is moving towards automation. Therefore, we are looking for you who are an automotive software test engineer or automotive software developer, preferably experienced with Python and Continuous Integration (CI/CD). Here, we encourage and support our engineers to evolve professionally as personally. Therefore, you will have the fullest support from your closest Jobba manager, who will follow you in your journey and support you forward – in the direction you want. When you feel like you want to learn something new, you can always take it into your own hands because Jobba Academy offers several educations, from new programming languages to negotiation skills and much more.</p><h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Job / Skills</h2><p>To be successful in this role, we believe that you have:</p> <ul><li>Minimum 5 years of experience working with automotive software, either testing or development.</li> <li>Professional experience working with Python or C++.</li> <li>Worked in an Agile environment.</li> <li>A relevant degree in Computer Science, Software Engineering, Electronics, Data Science, Mathematics, Physics or similar.</li> </ul><p>Meritorious experience:</p> <ul><li>Experience in PyTest or Robot Framework.</li> <li>Experience with CI/CD tools e.g. Jenkins.</li> <li>Experience with Vector tools e.g. CANoe, CANalyzer.</li> <li>Experience with CAN, LIN, Ethernet.</li> </ul><p>&nbsp;To succeed in the role as a consultant at Jobba you need to be analytical, have a great sense for quality, a positive attitude and you need to be a team-player. If You find this as an interesting next step and would like to get in touch with us, don’t hesitate to send in your application.&nbsp;</p> <p><strong>About JOBBA</strong></p> <p>Jobba is one of Europe’s largest technology and IT consulting companies with over 45,000 employees in over 30 countries. Our engineers carry out complex and highly technical projects throughout the value chain of the most prestigious companies in all sectors, such as Automotive, Telecom, Industry, Energy, Aerospace &amp; Defense and Life Science. In Sweden, we are over 1300 committed employees with 11 offices in 10 cities - from Lund in the south to Skellefteå in the north.</p> <p>For the fourth year in a row, Jobba has been named one of Sweden\'s most attractive employers by Karriärföretagen 2023, an award for employers that offer unique career and development opportunities.</p> <p>Welcome to read more about us at&nbsp;<a href="#" target="_blank" rel="noreferrer noopener">jobba.se</a></p> <p>We are looking forward to your application!</p>    </div>',
                                            'experience': '3+', 'expiry': '20/10/2023', 'id': '1001',
                                            'loc': 'Menlo Park', 'location': 'Jonkoping', 'postdate': '08/01/2019',
                                            'salary': '110000', 'title': 'Data Scientist', 'type': 'Full time'}}), (
                          '1002', {'Applicants': {
                              'abubakarkhan99': {'coverletter_name': ' sdfhj,kl.ukyuyhrsrfwergtshyjufyjh',
                                                 'email_name': 'abubakar_khan_99@hotmail.com',
                                                 'eu_eligible_name': 'yes', 'exp_name': '2', 'firstname_name': 'Hafiz',
                                                 'lastname_name': 'Khan', 'phonenum_name': '+46735625456',
                                                 'url_cv': 'https://firebasestorage.googleapis.com/v0/b/job-portal-c65be.appspot.com/o/files%2FInternational%20Deferral%20Form%20-%20NCIRL.pdf?alt=media'}},
                                   'Req': {'company': 'Amazon', 'deadline': '01/03/2023',
                                           'desc': '<div class="job-text">     <h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Personality / Commitment</h2><p><span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">To fit into this role, you need to have a personality that exudes drive and proactivity. </font><font style="vertical-align: inherit;">You are a problem-solving oriented and positive person who enjoys working in teams to jointly reach the best solution.</font></font><br> &nbsp;</span></p><h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Job / Skills</h2><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Now we have an opportunity for you who want to work in manufacturing. </font><font style="vertical-align: inherit;">The role is within production technology with a focus on PLC programming. </font><font style="vertical-align: inherit;">We are now looking for automation engineers with education or experience.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">As a consultant with us, you work with the main focus on PLC programming for one of our clients. </font><font style="vertical-align: inherit;">Furthermore, you get both a team feeling in your assignment and a really lovely community at ALTEN. </font><font style="vertical-align: inherit;">Through our internal networks ALTEN Sports, Women@ALTEN and ALTEN Innovation, you are given the opportunity to pursue issues and activities that you are passionate about, together with your colleagues. </font><font style="vertical-align: inherit;">Everything is of course voluntary. </font><font style="vertical-align: inherit;">We place balance between work and private life at the top of the list. </font><font style="vertical-align: inherit;">Of course, we have a collective agreement. </font><font style="vertical-align: inherit;">In addition to this, we have benefits such as health care allowance, occupational pension and insurance.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">We are looking for you as a manufacturing engineer as you join as a production technician with a focus on automation. </font><font style="vertical-align: inherit;">Together with other technicians in the area, you will drive technology development to reach the goals set for the area in the form of technical availability, production cost, ergonomics, volume and quality. </font><font style="vertical-align: inherit;">The role requires a genuine interest in technology, analytical ability and collaborative skills. </font><font style="vertical-align: inherit;">In the role, you have to manage stakeholders in the form of operators, production managers, PT colleagues, maintenance and suppliers.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">The challenges are to drive improvement work together with other support functions at the same time in close cooperation with our customer\'s suppliers. </font><font style="vertical-align: inherit;">The service requires a technical understanding, but also an understanding to deliver the product at the right cost and quality.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Our customer has challenges regarding automation in several areas, which will also be part of the service to provide assistance and training for current employees. </font><font style="vertical-align: inherit;">Driving the technical development of automation requires technical curiosity, as well as good collaboration skills as it will always take place in consultation with several stakeholders. </font><font style="vertical-align: inherit;">This will require a great focus on getting to know the process and its parameters, as well as understanding how the process affects outcomes on the product but also subsequent processes. </font><font style="vertical-align: inherit;">Furthermore, it becomes a challenge to be in a factory during start-up, where routines are under construction, both with regard to the process itself, but also organizationally. </font><font style="vertical-align: inherit;">In other words, you must be prepared for changes to occur.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Training:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">University education in mechanical engineering/automation.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Production technical training meritorious.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Competency requirements:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">PLC programming is a requirement.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Analytical ability. </font><font style="vertical-align: inherit;">Ability to understand and break down complex problems when troubleshooting, for example. </font><font style="vertical-align: inherit;">Genuine technical interest, as this is an area of \u200b\u200brapid technological development.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Good cooperation skills with other technicians, maintenance but also understanding of operators, production managers and their requirements for delivery.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Meritorious:</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge of CNC controllers and robot handling.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge in vision technology.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Experience of working within highly automated flows.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Knowledge</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Swedish in both speech and writing.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">English in both speech and writing.</font></font></li> </ul><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">&nbsp;Characteristics/values</font></font></p> <ul><li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Documented, thorough, quality conscious &amp; committed.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Good cooperation skills.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Technically interested in machines and processes.</font></font></li> <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Strong personal drive.</font></font></li> </ul><p><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">What do we offer?</font></font></strong></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Every employee is equally important in ALTEN\'s success! </font><font style="vertical-align: inherit;">We believe in growing together by offering opportunities, development and community. </font><font style="vertical-align: inherit;">ALTEN operates in several different industries, has a large variety of assignments, coaching managers and training via the ALTEN Academy, which means that it will always be possible to develop with us. </font><font style="vertical-align: inherit;">Your wishes guide your path forward. </font><font style="vertical-align: inherit;">Through our internal networks such as Women@ALTEN and ALTEN Sports, you are given the opportunity to pursue issues and activities that you are passionate about. </font><font style="vertical-align: inherit;">At ALTEN, we think it is important to have a balance between work and leisure, which is why we offer three extra days off per year. </font><font style="vertical-align: inherit;">With us, you are connected to a collective agreement and are offered benefits such as health benefits, occupational pension and insurance.</font></font></p> <p>&nbsp;<strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Om OLD</font></font></strong></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ALTEN is one of Europe\'s largest technology and IT consulting companies with over 45,000 employees in more than 30 countries. </font><font style="vertical-align: inherit;">Our engineers carry out complex and highly technical projects throughout the entire product development chain at the leading companies in several different industries such as Automotive, Telecom, Industry, Energy, Aviation and Defense as well as Life Science. </font><font style="vertical-align: inherit;">In Sweden, we are over 1,300 committed employees with 11 offices in 10 cities - from Lund in the south to Skellefteå in the north.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">For the third year in a row, ALTEN has been named one of Sweden\'s most attractive employers by Career Companies 2022, an award for employers that offer unique career and development opportunities.</font></font></p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Welcome to read more about us at&nbsp; </font></font><a href="https://www.alten.se/" target="_blank" rel="noreferrer noopener"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">alten.se</font></font></a></p> <p>&nbsp;</p> <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">A warm welcome with your application!</font></font></p>    </div>',
                                           'experience': '5+', 'expiry': '20/10/2023', 'id': '1002', 'loc': 'Seattle',
                                           'postdate': '08/01/2019', 'salary': '130000',
                                           'title': 'Production Techniques - Automation', 'type': 'Full time'}}), (
                          '1003', {'Req': {'company': 'Microsoft', 'deadline': '01/03/2023',
                                           'desc': 'As an AI Engineer at Microsoft, you will work on building and deploying advanced AI and machine learning systems. You will collaborate with a team of researchers and engineers to develop cutting-edge algorithms, and implement them in real-world applications. Minimum qualifications include a bachelors degree in Computer Science, Electrical Engineering, or a related field, and 2+ years of experience in AI or machine learning.',
                                           'experience': '2+', 'expiry': '20/10/2023', 'id': '1003', 'loc': 'Redmond',
                                           'postdate': '08/01/2019', 'salary': '100000', 'title': 'AI Engineer',
                                           'type': 'Full time'}}), ('1004', {
        'Req': {'company': 'Amazon', 'deadline': '01/03/2023',
                'desc': 'The DevOps Engineer will be responsible for designing, implementing, and maintaining the infrastructure and tools to support the development and deployment of software. You will work closely with development teams to understand their needs and provide solutions to improve the overall software delivery process. The ideal candidate will have experience with cloud infrastructure, automation, and continuous integration/delivery.',
                'experience': '5+', 'expiry': '20/10/2023', 'id': '1004', 'loc': 'Seattle', 'postdate': '08/01/2019',
                'salary': '130000', 'title': 'DevOps Engineer', 'type': 'Full time'}}), ('1006', {
        'Req': {'company': 'Microsoft', 'deadline': '01/03/2023',
                'desc': 'The AI Engineer will be responsible for designing, developing and deploying AI-based solutions to improve various aspects of the Microsoft product and services. You will work closely with cross-functional teams to understand business needs, identify opportunities, and deliver data-driven solutions. The ideal candidate will have a background in computer science or a related field, and have experience in machine learning, data mining and modeling.',
                'experience': '2+', 'expiry': '20/10/2023', 'id': '1006', 'loc': 'Redmond', 'postdate': '08/01/2019',
                'salary': '100000', 'title': 'ML Engineer', 'type': 'Full time'}}), ('1007', {
        'Req': {'company': 'Apple', 'deadline': '01/03/2023',
                'desc': 'The iOS Developer will be responsible for designing, developing and testing iOS applications. You will work closely with cross-functional teams to understand business needs, identify opportunities, and deliver high-quality solutions. The ideal candidate will have a background in computer science or a related field, and have experience in iOS development, Swift and Objective-C.',
                'experience': '5+', 'expiry': '10/10/2023', 'id': '1007', 'loc': 'Redmond', 'postdate': '08/01/2019',
                'salary': '100000', 'title': 'AI Engineer', 'type': 'Full time'}})])

    received_data = request.POST.get('getjobid_btn',
                                     None)  # this is where we get the data when a request has been made even from a previous page/html
    print('received data, job detail page ran', received_data)

    # #uncomment these 3 lines to get proper response back
    try:
        id = received_data.split('¤¤¤')[0]
        title = received_data.split('¤¤¤')[1]
        desc = received_data.split('¤¤¤')[2]
        context['id'] = id
        context['title'] = title
        context['desc'] = desc
        context['data'] = jobdic
    except AttributeError:
        context['id'] = 'some id'
        context['title'] = 'some title'
        context[
            'desc'] = '''<div class="job-text">     <h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Personality / Commitment</h2><p>At Nordic Solutions in Gothenburg, Sweden we work with some of Sweden’s largest automotive manufacturers within research and development. Now we are looking to expand our team of automotive software test engineers. Within the field of testing, the trend is moving towards automation. Therefore, we are looking for you who are an automotive software test engineer or automotive software developer, preferably experienced with Python and Continuous Integration (CI/CD). Here, we encourage and support our engineers to evolve professionally as personally. Therefore, you will have the fullest support from your closest Nordic Solutions manager, who will follow you in your journey and support you forward – in the direction you want. When you feel like you want to learn something new, you can always take it into your own hands because Nordic Solutions Academy offers several educations, from new programming languages to negotiation skills and much more.</p><h2 class="font-alt color-blue-light size-2 letter-spacing-extra-small">Job / Skills</h2><p>To be successful in this role, we believe that you have:</p> <ul><li>Minimum 5 years of experience working with automotive software, either testing or development.</li> <li>Professional experience working with Python or C++.</li> <li>Worked in an Agile environment.</li> <li>A relevant degree in Computer Science, Software Engineering, Electronics, Data Science, Mathematics, Physics or similar.</li> </ul><p>Meritorious experience:</p> <ul><li>Experience in PyTest or Robot Framework.</li> <li>Experience with CI/CD tools e.g. Jenkins.</li> <li>Experience with Vector tools e.g. CANoe, CANalyzer.</li> <li>Experience with CAN, LIN, Ethernet.</li> </ul><p>&nbsp;To succeed in the role as a consultant at Nordic Solutions you need to be analytical, have a great sense for quality, a positive attitude and you need to be a team-player. If You find this as an interesting next step and would like to get in touch with us, don’t hesitate to send in your application.&nbsp;</p> <p><strong>About Nordic Solutions</strong></p> <p>Nordic Solutions is one of Europe’s largest technology and IT consulting companies with over 45,000 employees in over 30 countries. Our engineers carry out complex and highly technical projects throughout the value chain of the most prestigious companies in all sectors, such as Automotive, Telecom, Industry, Energy, Aerospace &amp; Defense and Life Science. In Sweden, we are over 1300 committed employees with 11 offices in 10 cities - from Lund in the south to Skellefteå in the north.</p> <p>For the fourth year in a row, Nordic Solutions has been named one of Sweden's most attractive employers by Karriärföretagen 2023, an award for employers that offer unique career and development opportunities.</p> <p>Welcome to read more about us at&nbsp;<a href="#" target="_blank" rel="noreferrer noopener">Nordic Solutions.se</a></p> <p>We are looking forward to your application!</p>    </div>'''
        context['data'] = jobdic

    # data=db.child('Jobs').child('Job Detail').get(id).val()
    # print(data['desc'])
    print('apply page called', context['id'])
    # if 'data' in request.GET:
    #     print('yes data is avail')
    # Context is the data that we need to send to the html while rendering
    return render(request, 'job_detail_pg.html', {
        'job_id': context})
def rfilldata(request):
    sentences = []
    if request.method == 'POST' and request.FILES.get('file'):
        context = {}
        print('file is selected now')
        import requests
        file = request.FILES.get('file')
        api_key = 'K89089545688957'
        url_api = 'https://api.ocr.space/parse/image'
        # Set the file path to upload
        file_path = file
        print('path')
        print(file_path)
        # Set language parameter if needed
        language = 'eng'
        # Set other parameters if needed
        is_overlay_required = False
        # Set the HTTP headers for the POST request
        headers = {'apikey': api_key}
        # Set the payload for the POST request
        payload = {'language': language, 'isOverlayRequired': is_overlay_required}
        # Upload the file and get the response
        response = requests.post(url_api, headers=headers, data=payload, files={'image': file_path})
        # Parse the response JSON

        # response = {'ParsedResults': [{'TextOverlay': {'Lines': [], 'HasOverlay': False,
        #                                                'Message': 'Text overlay is not provided as it is not requested'},
        #                                'TextOrientation': '0', 'FileParseExitCode': 1,
        #                                'ParsedText': "CONTACT ME AT\r\numar.farooq407@email.com\r\nhttps://www.linkedin.com/in/u\r\nmar•farooq• khan-107494167/\r\n*923365297082\r\n12-12-1997\r\nPROGRAMMING\r\nLANGUAGES\r\nPYTHON\r\nANDROID\r\nJAVA\r\nKOTLIN\r\nJAVASCRIPT/TYPESCRIPT\r\nHTML\r\nCLIENT-SIDE\r\nANDROID DEVELOPMENT\r\nANGULAR/ NODEJS\r\nFLASK\r\nDATABASE\r\nFIREBASE\r\nMICROSOFT SQL SERVER\r\nMYSQL\r\nACHEIVEMENTS\r\nLEVEL 2 SELLER ON FIVERR\r\nLEVEL SELLER ON\r\nUMAR FAROOQ KHAN\r\nSOFTWARE DEVELOPER\r\nPERSONAL PROFILE\r\nA full-stack software developer with holistic knowledge Of Android and Web\r\nDevelopment along with Python. Experienced in A1 and Data Science\r\nTechniques.\r\nWORK EXPERIENCE\r\nAndroid Developer (Remote Location)\r\nLesptitsmonstres I Montpellier, France I Aug 2019- February 2021\r\n• App Development in Native Android Platform with Android SDK/Java.\r\n• Using the Google Firebase (No-SQL database) and XML layout.\r\n• Manual Quality Assurance (QA), Maintainance, and Scaling.\r\nAndroid Developer (Contract, Remote Location)\r\nBothofus I Stockholm, Sweden September 2020\r\n• Figma IJI/UX Mockup Translation into Android screens by XML with\r\nfunctionality.\r\n• Firebase Push Notification and Rest API implementation for server calls.\r\n• Implementation of logo animation with Java/kotlin.\r\nKotlin Developer Intern\r\nE-conceptions I Islamabad, Pakistan I June 2019- July 2019\r\n• Support for basic programming: abstraction, inheritance, exception\r\nhandling, and polymorphism using Kotlin.\r\n• Support for implementation of lottery-checker automation tool.\r\nSocial Media Forensics, Data Science Intern\r\nNational Center for Cyber Security Islamabad I May 2019-July 2019\r\n• Development of Regional Database with Twitter API tweepy using Python.\r\n• Manual Labelling of the dataset into multi-label and multi-classes.\r\n• Implementation of exploration of trend (hashtag) origination on social\r\nmedia using GPS location information present in dataset.\r\nSentiment Analysis on Local Regional Data of Twitter with Machine\r\nLearning ( Bachelor's Thesis )\r\n• A project backed by the National Center for Cyber Security (NCCS), an\r\nagency commissioned by the Government of Pakistan.\r\n• GetOldTweets python API for fetching Twitter data.\r\n• Preprocessing of the dataset using Regex and Pandas Python Library.\r\n• Implementation of SVM and Naive Bayes algorithms in Python with the\r\nSklearn and Machine Learning (ML) algorithms with an accuracy of 97%.\r\n• Front-End on Flask and the Back-End on Python.\r\n",
        #                                'ErrorMessage': '', 'ErrorDetails': ''}, {
        #                                   'TextOverlay': {'Lines': [], 'HasOverlay': False,
        #                                                   'Message': 'Text overlay is not provided as it is not requested'},
        #                                   'TextOrientation': '0', 'FileParseExitCode': 1,
        #                                   'ParsedText': "CONTACT ME AT\r\numar.farooq407@gmail.com\r\nhttps:/\\www.linkedin.com/in/u\r\n*923365297082\r\nPROJECTS\r\n• Job Portal Website: Job portal website made from Django web\r\nframework\r\n• Pulsar: A news aggregator website using Angular & Nodejs.\r\nTailored/customized newsfeed using ML and A1 algorithms to show\r\nrelated news from different news sources.\r\n• Career Counseling Platform: A career counseling website made from\r\nAngular & Nodejs where students, job seekers, and one who wants to\r\nswitch their career can seek guidance from top leading career\r\ncounselling coaches.\r\n• Blood Donation App: An android app for Urgent Blood Donation and for\r\nFinding Donors.\r\n• News journal priorities on UN SGD: Extensive work on web Scraping and\r\nDetailed Sentiment Analysis and comparison of priorities of UN SGD\r\ngoals on 3 top American News journals\r\n• Spanish Tweets Sentiment Analysis: Spanish tweets were scraped by\r\nthe Tweepy API of some political parties and then classified and\r\nanalyzed the sentiments.\r\n• What's My Profit: E-commerce Income Calculator: Automation tool that\r\ncalculates various income sources files and converts sales into local\r\ncurrency at an exchange rate\r\nEDUCATIONAL HISTORY\r\nBachelor Of Science in Computer Science (BSCS)\r\nAir University, Islamabad | 2016-2020\r\n• Relevant Subjects: Data Science, Information & Network Security,\r\nAndroid Development, Full Stack Web Development (MEAN), Digital\r\nImage Processing, Human-Machine Interaction (HMI), Software\r\nEngineering, Visual Programming C#, Data Structure & Algorithms, Intro\r\nto A1, Computer Architecture, Operating Systems (Linux Environment),\r\nAssembly Language\r\nPre-Engineering, High School\r\nICB G-6/3 1 Islamabad, Pakistan | 2013-2015\r\nLANGUAGES\r\n• English (Fluent)\r\n• Urdu(Fluent)\r\nEXTRACURRICULAR ACTIVITIES\r\n• Cricket\r\n• Writing Programming Articles (Medium.com\r\n• YouTube Content Creation Cinematogra&y-\r\n• Photography, Travelling\r\n",
        #                                   'ErrorMessage': '', 'ErrorDetails': ''}], 'OCRExitCode': 1,
        #             'IsErroredOnProcessing': False, 'ProcessingTimeInMilliseconds': '2984',
        #             'SearchablePDFURL': 'Searchable PDF not generated as it was not requested.'}
        # ocr_text = response.json()
        ocr_text = response
        # Print the response JSON
        print(ocr_text)
        data1 = []
        data1.append(ocr_text['ParsedResults'][0]['ParsedText'])
        # this is where we get the data when a request has been made even from a previous page/html
        ind = ''.join(data1).split('EXPERIENCE')
        mylist = ind[1]
        sentences = mylist
        print('sentences again refresh')
        print(sentences)
        datatopush = {'tempdata': sentences}
        #db.child('Jobs').child('temp').set(datatopush)
        request.session['jd'] = sentences



    if request.method == 'GET':
        print(     'refreshed get called')
        id = 'some,id'
        title = 'some,title '
        desc = 'some,desc'
        jd = 'some jd in GET 153 line'
    context = {}
    received_data_fromhtml = request.POST.get('getjobid_btn', None)  # this is where we get the data when a request has been made even from a previous page/html
    received_data = request.POST.get('getjobid_btn',
                                     None)  # this is where we get the data when a request has been made even from a previous page/html
    print('r job detail page ran', received_data)
    try:
        id = received_data.split(',')[0]
        title = received_data.split(',')[1]
        context['id'] = id
        context['title'] = title
        #context['jd'] = 'job desc before It is set.'


    except AttributeError:
        print('refreshed')
        id = 'Some Id'
        title = 'some title '
        desc = 'some desc'
        context['id'] = id
        context['title'] = title
        context['jd'] = sentences
        received_data = '1001'

    # Context is the data that we need to send to the html while rendering

    return render(request, 'applypage_html.html', {
        'job_id': context})


def applied(request):

    print('applied function called from starting')

    received_data_fromhtml = request.POST.get('getjobid_btn',
                                              None)  # this is where we get the data when a request has been made even from a previous page/html
    print(received_data_fromhtml)
    if request.method == 'POST':
        print('post data in applied func', request.POST)
        # job_id = context['applybtn']
        a = request.POST['firstname_name']
        b = request.POST['lastname_name']
        c = request.POST['email_name']
        d = request.POST['phonenum_name']
        e = request.POST['coverletter_name']
        f = request.POST['exp_name']
        g = request.POST['eu_eligible_name']
        id = request.POST['submit_html']


        file = request.FILES.get('file_html')
        from_date_input = request.POST.getlist('fromdate_input')
        to_date_input = request.POST.getlist('todate_input')
        jd_input = request.POST.getlist('jd_input')
        company_input = request.POST.getlist('company_input')
        storage.child('files/' + file.name).put(file)
        # print('filepath',file_path)
        # print(storage.child('files').put(file_cv))
        url = storage.child('files/' + file.name).get_url(token=None)
        context = {}
        request.session['id'] = id
        request.session['email_name'] = c

        datatopush = {'firstname_name': a, 'lastname_name': b, 'email_name': c, 'phonenum_name': d,
                      'coverletter_name': e, 'exp_name': f, 'eu_eligible_name': g, 'url_cv': url,
                      'job_fromdatelist': from_date_input,'job_todatelist': to_date_input,   'companylist': company_input, 'job_desc_list': jd_input, 'loc':  request.POST.getlist('location_input'), 'Job Title':  request.POST.getlist('job_title_input')}
        db.child('Jobs').child('Job Detail').child(id).child('Applicants').child(
            c.split('@')[0].replace('.', '').replace('_', '')).set(datatopush)

        jd_data_fromprev = request.session.get('jd', 'default_value')

        #print('session data')
        #print(jd_data_fromprev)

        #no need to get data from firebase, I just used session storage in order to pass the data
        #jd_fromdb = db.child('Jobs').child('temp').get().val()

        if any(not x for x in company_input + from_date_input + to_date_input + jd_input):
            print("At least one field is empty.")
            context['job_details'] = jd_data_fromprev
            return render(request, 'apply_success_not_filled.html', context={'data_successpage': context})

        print('He already filled everything')
        return render(request, 'apply_success_already_filled.html')

    # if request.method == 'POST' and request.FILES.get('file'):
    #     print('file is selected now')
    #     import requests
    #     file = request.FILES.get('file')
    #     api_key = 'K89089545688957'
    #     url_api = 'https://api.ocr.space/parse/image'
    #     # Set the file path to upload
    #     file_path = file
    #     print('path')
    #     print(file_path)
    #     # Set language parameter if needed
    #     language = 'eng'
    #     # Set other parameters if needed
    #     is_overlay_required = False
    #     # Set the HTTP headers for the POST request
    #     headers = {'apikey': api_key}
    #     # Set the payload for the POST request
    #     payload = {'language': language, 'isOverlayRequired': is_overlay_required}
    #     # Upload the file and get the response
    #
    #     # response = requests.post(url_api, headers=headers, data=payload, files={'image': file_path})
    #     # Parse the response JSON
    #     response = {}
    #     response = {'ParsedResults': [{'TextOverlay': {'Lines': [], 'HasOverlay': False,
    #                                                    'Message': 'Text overlay is not provided as it is not requested'},
    #                                    'TextOrientation': '0', 'FileParseExitCode': 1,
    #                                    'ParsedText': "CONTACT ME AT\r\numar.farooq407@email.com\r\nhttps://www.linkedin.com/in/u\r\nmar•farooq• khan-107494167/\r\n*923365297082\r\n12-12-1997\r\nPROGRAMMING\r\nLANGUAGES\r\nPYTHON\r\nANDROID\r\nJAVA\r\nKOTLIN\r\nJAVASCRIPT/TYPESCRIPT\r\nHTML\r\nCLIENT-SIDE\r\nANDROID DEVELOPMENT\r\nANGULAR/ NODEJS\r\nFLASK\r\nDATABASE\r\nFIREBASE\r\nMICROSOFT SQL SERVER\r\nMYSQL\r\nACHEIVEMENTS\r\nLEVEL 2 SELLER ON FIVERR\r\nLEVEL SELLER ON\r\nUMAR FAROOQ KHAN\r\nSOFTWARE DEVELOPER\r\nPERSONAL PROFILE\r\nA full-stack software developer with holistic knowledge Of Android and Web\r\nDevelopment along with Python. Experienced in A1 and Data Science\r\nTechniques.\r\nWORK EXPERIENCE\r\nAndroid Developer (Remote Location)\r\nLesptitsmonstres I Montpellier, France I Aug 2019- February 2021\r\n• App Development in Native Android Platform with Android SDK/Java.\r\n• Using the Google Firebase (No-SQL database) and XML layout.\r\n• Manual Quality Assurance (QA), Maintainance, and Scaling.\r\nAndroid Developer (Contract, Remote Location)\r\nBothofus I Stockholm, Sweden September 2020\r\n• Figma IJI/UX Mockup Translation into Android screens by XML with\r\nfunctionality.\r\n• Firebase Push Notification and Rest API implementation for server calls.\r\n• Implementation of logo animation with Java/kotlin.\r\nKotlin Developer Intern\r\nE-conceptions I Islamabad, Pakistan I June 2019- July 2019\r\n• Support for basic programming: abstraction, inheritance, exception\r\nhandling, and polymorphism using Kotlin.\r\n• Support for implementation of lottery-checker automation tool.\r\nSocial Media Forensics, Data Science Intern\r\nNational Center for Cyber Security Islamabad I May 2019-July 2019\r\n• Development of Regional Database with Twitter API tweepy using Python.\r\n• Manual Labelling of the dataset into multi-label and multi-classes.\r\n• Implementation of exploration of trend (hashtag) origination on social\r\nmedia using GPS location information present in dataset.\r\nSentiment Analysis on Local Regional Data of Twitter with Machine\r\nLearning ( Bachelor's Thesis )\r\n• A project backed by the National Center for Cyber Security (NCCS), an\r\nagency commissioned by the Government of Pakistan.\r\n• GetOldTweets python API for fetching Twitter data.\r\n• Preprocessing of the dataset using Regex and Pandas Python Library.\r\n• Implementation of SVM and Naive Bayes algorithms in Python with the\r\nSklearn and Machine Learning (ML) algorithms with an accuracy of 97%.\r\n• Front-End on Flask and the Back-End on Python.\r\n",
    #                                    'ErrorMessage': '', 'ErrorDetails': ''}, {
    #                                       'TextOverlay': {'Lines': [], 'HasOverlay': False,
    #                                                       'Message': 'Text overlay is not provided as it is not requested'},
    #                                       'TextOrientation': '0', 'FileParseExitCode': 1,
    #                                       'ParsedText': "CONTACT ME AT\r\numar.farooq407@gmail.com\r\nhttps:/\\www.linkedin.com/in/u\r\n*923365297082\r\nPROJECTS\r\n• Job Portal Website: Job portal website made from Django web\r\nframework\r\n• Pulsar: A news aggregator website using Angular & Nodejs.\r\nTailored/customized newsfeed using ML and A1 algorithms to show\r\nrelated news from different news sources.\r\n• Career Counseling Platform: A career counseling website made from\r\nAngular & Nodejs where students, job seekers, and one who wants to\r\nswitch their career can seek guidance from top leading career\r\ncounselling coaches.\r\n• Blood Donation App: An android app for Urgent Blood Donation and for\r\nFinding Donors.\r\n• News journal priorities on UN SGD: Extensive work on web Scraping and\r\nDetailed Sentiment Analysis and comparison of priorities of UN SGD\r\ngoals on 3 top American News journals\r\n• Spanish Tweets Sentiment Analysis: Spanish tweets were scraped by\r\nthe Tweepy API of some political parties and then classified and\r\nanalyzed the sentiments.\r\n• What's My Profit: E-commerce Income Calculator: Automation tool that\r\ncalculates various income sources files and converts sales into local\r\ncurrency at an exchange rate\r\nEDUCATIONAL HISTORY\r\nBachelor Of Science in Computer Science (BSCS)\r\nAir University, Islamabad | 2016-2020\r\n• Relevant Subjects: Data Science, Information & Network Security,\r\nAndroid Development, Full Stack Web Development (MEAN), Digital\r\nImage Processing, Human-Machine Interaction (HMI), Software\r\nEngineering, Visual Programming C#, Data Structure & Algorithms, Intro\r\nto A1, Computer Architecture, Operating Systems (Linux Environment),\r\nAssembly Language\r\nPre-Engineering, High School\r\nICB G-6/3 1 Islamabad, Pakistan | 2013-2015\r\nLANGUAGES\r\n• English (Fluent)\r\n• Urdu(Fluent)\r\nEXTRACURRICULAR ACTIVITIES\r\n• Cricket\r\n• Writing Programming Articles (Medium.com\r\n• YouTube Content Creation Cinematogra&y-\r\n• Photography, Travelling\r\n",
    #                                       'ErrorMessage': '', 'ErrorDetails': ''}], 'OCRExitCode': 1,
    #                 'IsErroredOnProcessing': False, 'ProcessingTimeInMilliseconds': '2984',
    #                 'SearchablePDFURL': 'Searchable PDF not generated as it was not requested.'}
    #
    #     # ocr_text = response.json()
    #     ocr_text = response
    #
    #     # Print the response JSON
    #     print(ocr_text)
    #     data1 = []
    #     data1.append(ocr_text['ParsedResults'][0]['ParsedText'])
    #     nlp = spacy.load("en_core_web_sm")
    #
    #     ind = ''.join(data1).split('EXPERIENCE')
    #     mylist = ind[1]
    #     sentences = mylist






def success(request):
    print('success func caleld')
    if request.method == 'POST':
        date_input = request.POST.getlist('date_input')
        jd_input = request.POST.getlist('jd_input')
        company_input = request.POST.getlist('company_input')
        from_date_input = request.POST.getlist('fromdate_input')
        to_date_input = request.POST.getlist('todate_input')

        datatopush = {  'job_fromdatelist': from_date_input,'job_todatelist': to_date_input , 'job_datelist': date_input, 'companylist': company_input, 'job_desc_list': jd_input , 'loc':  request.POST.getlist('location_input'), 'Job Title':  request.POST.get('job_title_input') }
        id = request.session.get('id', 'default_value')
        c = request.session.get('email_name', 'default_value')

        db.child('Jobs').child('Job Detail').child(id).child('Applicants')\
            .child(c.split('@')[0].replace('.', '').replace('_', '')).update(datatopush)
        recipient_list = [c]
        subject = 'Job Applied Successfully'
        message = 'You have successfully applied for the position'
        email_from = 'umar.farooq407@gmail.com'

        #send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        return render(request, 'apply_success_already_filled.html')

    return render(request, 'apply_success_already_filled.html')

@csrf_protect
def your_django_function(request):
    from django.views.decorators.csrf import csrf_protect
    print('file chonse')
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        print('file chonse')
        print(file)
        return HttpResponse('x', status=200)
        # Process the file here
def load_more(request):
    # Your logic to fetch more data and generate HTML goes here
    context = {}
    print('loadddddd')
    context['newid'] = 2
    return render(request, 'load-more.html', {'uniqueid': context})