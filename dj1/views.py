#first fie
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase
import datetime
import random
config = {
  "apiKey": "AIzaSyDwavVG6PDP-LWqJbVBvFoSSk8h16jwmM8",
  "authDomain": "djangoproj-91428.firebaseapp.com",
  "databaseURL": "https://djangoproj-91428-default-rtdb.firebaseio.com",
  "projectId": "djangoproj-91428",
  "storageBucket": "djangoproj-91428.appspot.com",
  "messagingSenderlId": "15636136866",
  "appId": "1:15636136866:web:eba927ac49ce031edbe8fb",
  "measurementId": "G-D9GR157PPH"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
l=['a','b','c','d','e','f','g','h']
l2=['I','J','K','L','M','N','O','P']
l3=['@','₹','&','*','+','-']
Cookie = ""
Cookie += random.choice(l)
Cookie += random.choice(l2)
Cookie += random.choice(l3)

def index(requests):
    sess = requests.COOKIES['session']
    if sess == Cookie :
        frmt = requests.POST.get("format")
        txt = requests.POST.get("text")
        return render(requests ,"index.html",{'code': txt})
    else:
        frmt = requests.POST.get("format")
        txt = requests.POST.get("text")
        return render(requests,"index2.html",{'code': txt})
def SignIn(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	return render(requests, "SignIn.html")
def change(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	try : 
		user = auth.sign_in_with_email_and_password(id,pas)
		response = render(requests, "index.html")
		response.set_cookie('session', Cookie)
		return response
	except :
		message = "wrong email id or password"
		return render(requests,"SignIn.html",{'msg': message})
def SignUp(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	return render(requests, "SignUp.html")
def postSignUp(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	try : 
		user = auth.create_user_with_email_and_password(id,pas)
		response = render(requests, "index.html")
		response.set_cookie('session', Cookie)
		return response
	except :
		return render(requests,"SignUp.html")
	session_id=user['idToken']
	request.session['uid']=str(session_id)
	return render(requests,"postSignUp.html")
def message(requests):
	return render(requests,"messanger.html")
def fill(requests):
    return render(requests,"create.html")
def create(requests):
    return render(requests, 'index.html')