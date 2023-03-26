# pip install -U spacy
# python -m spacy download en_core_web_sm
#import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = (''' 
Android Developer (Remote Location)
Lesptitsmonstres I Montpellier, France I Aug 2019- February 2021
• App Development in Native Android Platform with Android SDK/Java.
• Using the Google Firebase (No-SQL database) and XML layout.
• Manual Quality Assurance (QA), Maintainance, and Scaling.
Android Developer (Contract, Remote Location)
Bothofus I Stockholm, Sweden September 2020
• Figma IJI/UX Mockup Translation into Android screens by XML with
functionality.
• Firebase Push Notification and Rest API implementation for server calls.
• Implementation of logo animation with Java/kotlin.
Kotlin Developer Intern
E-conceptions I Islamabad, Pakistan I June 2019- July 2019
• Support for basic programming: abstraction, inheritance, exception
handling, and polymorphism using Kotlin.
• Support for implementation of lottery-checker automation tool.
Social Media Forensics, Data Science Intern
National Center for Cyber Security Islamabad I May 2019-July 2019
• Development of Regional Database with Twitter API tweepy using Python.
• Manual Labelling of the dataset into multi-label and multi-classes.
• Implementation of exploration of trend (hashtag) origination on social
media using GPS location information present in dataset.
Sentiment Analysis on Local Regional Data of Twitter with Machine
Learning ( Bachelor's Thesis )
• A project backed by the National Center for Cyber Security (NCCS), an
agency commissioned by the Government of Pakistan.
• GetOldTweets python API for fetching Twitter data.
• Preprocessing of the dataset using Regex and Pandas Python Library.
• Implementation of SVM and Naive Bayes algorithms in Python with the
Sklearn and Machine Learning (ML) algorithms with an accuracy of 97%.
• Front-End on Flask and the Back-End on Python.
''')
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
