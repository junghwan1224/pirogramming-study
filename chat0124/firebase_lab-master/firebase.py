import pyrebase

firebase = pyrebase.initialize_app({
    'apiKey': "AIzaSyAC0ewQ0O1LxNg_ypr-aCr2l41UhdldYXE",
    'authDomain': "gongmoowon-f8d6f.firebaseapp.com",
    'databaseURL': "https://gongmoowon-f8d6f.firebaseio.com/",
    'storageBucket': ""
    })
firebase_db = firebase.database()
