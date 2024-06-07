from flask import Flask,render_template,jsonify,redirect
 
import os
import socket
app=Flask(__name__)
 
#find the hostname and machine ip
listmaximum=[20,60,70,90,500,700,800,99]
def findhostname():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)

def findaddress():
    phone_number="4049931269"
    emailaddress="paul.fatoki.itb@gmail.com"
    comp="6616 heben ct., camby"
    
    return str(phone_number),str(emailaddress),str(comp)


@app.route("/")
def home():
    return "welcome to my hyperdrive page"

@app.route("/score")
def score():
    a=2000
    b=250
    result=a+b
    name = "paul"
    return render_template("index.html",name=name)
    #return str(result)


    
@app.route("/details")
def hostname():
    myhost,myip=findhostname()
    return render_template('show.html',host=myhost,IP=myip)


   

    
if __name__ == '__main__':
    app.run(debug=True, port=5008
            ,host="127.0.0.1")
