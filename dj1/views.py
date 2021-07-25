#first fie
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import pyrebase
import datetime
import itertools
import random
from json import dumps
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
def set_cookie(response, key, value, days_expire= 30):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE,
    )
def data():
    d = database.child("data").shallow().get().val()
    print(d)
    titles = []
    for i in d:
        titles.append(i)
    user = []
    title = []
    code = []
    discription = []
    for i in titles:
        u = database.child("data").child(i).child("usr").get().val()
        t = database.child("data").child(i).child("title").get().val()
        c = database.child("data").child(i).child("code").get().val()
        d = database.child("data").child(i).child("discription").get().val()
        user.append(u)
        title.append(t)
        code.append(c)
        discription.append(d)
    final = zip(user,title,code,discription)
    return final
def index(requests):
    try:
        sess = requests.COOKIES['session']
    except:
        give = data()
        return render(requests,"index2.html",{'a' : give})
    if sess :
        give = data()
        title = requests.POST.get("title")
        txt = requests.POST.get("text")
        disc = requests.POST.get("discription")
        tit = None
        if title :
            tit = "--"+title
            dic = {'code': txt,'usr': sess,'title': title,'discription': disc }
            database.child("data").child(tit).set(dic)
        return render(requests ,"index.html",{"a": give})
def SignIn(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	return render(requests, "SignIn.html")
def postSignIn(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	try : 
		user = auth.sign_in_with_email_and_password(id,pas)
		response = render(requests, "index.html")
		#response.set_cookie('session', "signup")
		return response
	except :
		message = "wrong email id or password"
		return render(requests,"SignIn.html",{'msg': message})
def SignUp(requests):
	pas = str(requests.POST.get("password"))
	id = requests.POST.get("email id")
	return render(requests, "SignUp.html")
def postSignUp(requests):
    usr = requests.POST.get("username")
    pas = str(requests.POST.get("password"))
    pas2 = str(requests.POST.get("password2"))
    if pas2 != pas:
        message = "passwords dosen't match please try again"
        return render(requests,"SignUp.html",{'msg': message})
    try :
        id = requests.POST.get("email id")
        user = auth.create_user_with_email_and_password(id,pas)
        response = render(requests, "index.html")
        set_cookie(response,"session",usr)
        return response
    except :
        return render(requests,"SignUp.html")
    return render(requests,"postSignUp.html")
def fill(requests):
    return render(requests,"create.html")
def create(requests):
    return render(requests, 'index.html')