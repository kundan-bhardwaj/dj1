#first file
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase
config = {
  "apiKey": "AIzaSyDwavVG6PDP-LWqJbVBvFoSSk8h16jwmM8",
  "authDomain": "djangoproj-91428.firebaseapp.com",
  "databaseURL": "https://djangoproj-91428-default-rtdb.firebaseio.com",
  "projectId": "djangoproj-91428",
  "storageBucket": "djangoproj-91428.appspot.com",
  "messagingSenderId": "15636136866",
  "appId": "1:15636136866:web:eba927ac49ce031edbe8fb",
  "measurementId": "G-D9GR157PPH"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
def index(requests):
	return render(requests ,"index.html")
def SignIn(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	return render(requests, "SignIn.html")
def change(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	try : 
		user = auth.sign_in_with_email_and_password(id,pas)
	except :
		message = "wrong email id or password"
		return render(requests,"SignIn.html",{'msg': message})
	return render(requests, "page1.html")
def SignUp(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	return render(requests, "SignUp.html")
def postSignUp(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	try : 
		user = auth.create_user_with_email_and_password(id,pas)
	except :
		pass
	return render(requests,"postSignUp.html")
def message(requests):
	return render(requests,"messanger.html")