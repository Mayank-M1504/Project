
import json
from werkzeug.security import generate_password_hash,check_password_hash
from flask import request
from flask import Flask,redirect,render_template,flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_required,logout_user,current_user,login_manager,LoginManager,login_user
from flask.helpers import url_for
import mysql.connector


#database connection
local_server=True
app=Flask(__name__)
app.secret_key="MayankM"


#for getting access
login_manager=LoginManager(app)
login_manager.login_view='login'


app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/bloodbank'
db=SQLAlchemy(app)

with open('config.json','r') as c:
    params=json.load(c)["params"]

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 

class custfeed(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    feedback=db.Column(db.String(200)) 

 

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    password=db.Column(db.String(1000)) 
 
class Bloodreq(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.String(15))
    qty=db.Column(db.Integer)
    reason=db.Column(db.String(100))
 
class Blood(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.String(15))
    qty=db.Column(db.Integer)
    doctorid=db.Column(db.Integer)
    disesase=db.Column(db.String(50))
    
@app.route("/index")
def index():
    return render_template("index.html")
 

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/usersignup")
def usersignup():
    return render_template("usersignup.html")

@app.route("/requestb")
def requestb():
    return render_template("request.html")
    
@app.route("/userlogin")
def userlogin():
    return render_template("userlogin.html")

@app.route("/adminlogin")
def adminlogin():
    return render_template("adminlogin.html")

@app.route("/adminpage")
def adminpage():
    return render_template("adminpage.html")


@app.route('/signup',methods=['POST','GET'])   
def signup():
    if request.method=="POST":
        id=request.form.get('id')     
        name=request.form.get('name')     
        email=request.form.get('email')  
        password=request.form.get('password')     
        #print(userid,name,email,password)
        encpassword=generate_password_hash(password)
        user1=User.query.filter_by(id=id).first()
        email1=User.query.filter_by(email=email).first()

        if user1 or email1 :
            return render_template("userlogin.html")
        
        new_user= db.engine.execute(f"INSERT INTO user (id,name,email,password) VALUES ('{id}','{name}','{email}','{encpassword}')")

        return render_template("userlogin.html")
    return render_template("usersignup.html")


@app.route('/login',methods=['POST','GET'])   
def login():
    if request.method=="POST":     
        id=request.form.get('id')  
        password=request.form.get('password') 
        # print(id,password)
        user=User.query.filter_by(id=id).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            return render_template("index.html")
        
        else:
            flash("Invalid User ID or Password","danger")
            return render_template("userlogin.html")
        
@app.route('/logout')
@login_required   
def logout():
    logout_user()
    return redirect("/")



@app.route('/admin',methods=['POST','GET'])   
def admin():
    if request.method=="POST":     
        username=request.form.get('username')  
        password=request.form.get('password')
    if (username==params['username'] and password==params['password']):
        session['user']=username
        return render_template("adminpage.html")
    else:
        flash("Invalid Username or Password")
        return render_template("adminlogin.html")


@app.route('/logoutadmin')
def logoutadmin():
    session.pop('user')
    return redirect("/")


@app.route('/adminadd',methods=['POST','GET'])   
def adminadd():
    if ('user' in session and session['user']==params['username']):
        if request.method=="POST":
            type=request.form.get('type')     
            doctorid=request.form.get('doctorid')     
            disease=request.form.get('disease') 
            qty=request.form.get('qty') 
            new_user= db.engine.execute(f"INSERT INTO blood (type,qty,doctorid,disease) VALUES ('{type}','{qty}','{doctorid}','{disease}')")
            flash("Succesfully Added Blood")
            return render_template("adminpage.html")
    else:
        return redirect('/adminlogin')
    
        
@app.route("/reqblood",methods=['POST','GET'])
def requestblood():
    if request.method=="POST":
        type=request.form.get('type')
        bqty=request.form.get('qty')
        reason=request.form.get('reason')
        dbb=db.engine.execute(f"UPDATE `blood` SET `qty`=`qty`-'{bqty}' WHERE `type` ='{type}' AND `blood`.`qty` >= '{bqty}'") 
        flash("Successful")
        return render_template("request.html")
    else:
        flash("Not Availavble")
        return render_template("request.html")
    

@app.route('/blood-details')
def blood_details():
    rows=db.engine.execute(F"SELECT * FROM `Blood`")
    # print(rows)
    return render_template('blood_details.html', rows=rows)
            

@app.route("/feedback",methods=['POST','GET'])
def feedback():
    if request.method=="POST":
        id=request.form.get('id')
        email=request.form.get('email')
        feedback=request.form.get('feedback')
        dbb=db.engine.execute(f"INSERT INTO `custfeed` (`id`,`email`,`feedback`) VALUES ('{id}','{email}','{feedback}')") 
        return render_template("request.html")
    


@app.route('/custfeedback')
def custfeedback():
    rows=db.engine.execute(F"SELECT * FROM `custfeed`")
    return render_template('feedback.html', rows=rows)



        # btype=type
        # dbb=db.engine.execute(f"SELETC * FROM `blood`  WHERE `blood`.`type` ='{btype}'")
        # type=type
        # if type=="A":
        #     for d in dbb:
        #         quantity=d.qty
        #         print(quantity)
        #         ar=Blood.query.filter_by(type=btype).first()
        #         ar.type=qty-1
        #         db.session.commiut()


    

app.run(debug=True)

