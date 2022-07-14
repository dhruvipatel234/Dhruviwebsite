

from unittest import result
import PyPDF2
import re
from webbrowser import get
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect,session,flash,send_from_directory, url_for,\
    request
import os
from flask_mysqldb import MySQL
from datetime import date
from datetime import timedelta
from flask_mail import Mail, Message
from sqlalchemy import false, true, values



app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dhruvikaneriya52@gmail.com'
app.config['MAIL_PASSWORD'] = 'mtzfueqfvwitrhwx'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


app.secret_key='sanskar'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Sanskar'
app.config['MYSQL_DB']='system'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.permanent_session_lifetime = timedelta(minutes=100000)
app.config['UPLOAD_FOLDER'] = "static/profilephoto/"
app.config['UPLOAD_FOLDER_A'] = "static/pdf/"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
  
ALLOWED_EXTENSIONS = set(['png', 'jpg'])
  
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

db=MySQL(app)

@app.route("/")
def choice():
    if 'userloggedin' in session :
            flash('you alredy login our site')
            return redirect('userhome')
    
    else:
        if 'loggedin' in session:
            flash('you alredy login our site')
            return redirect('admin_home')
        else:
            return render_template('main.html')

@app.route("/admin_first")
def admin_first():
    return render_template('admin_first.html')

@app.route('/admin_logout')
def admin_logout():
    session['loggedin'] = False
   
    session.clear()
    
    flash('you sucseesfully logout')
    return render_template("main.html")

@app.route('/user_logout')
def userlogout():
    session['userloggedin'] = False
    session.clear()
    flash('you sucseesfully logout')
    return render_template("main.html")


#=====================  ADMIN LOGIN ============================================================

@app.route("/admin_login" ,methods=['GET', 'POST'])
def admin_login():
    
        if request.method == 'POST':
                femail =request.form.get("email")
                fpassword=request.form.get("repassword")    

                if femail=="" or fpassword=="":
                    error="email and password are not blank" 
                    return render_template("admin_login.html",error=error)     

                cur = db.connection.cursor() 
                cur.execute('SELECT * FROM Admin_login WHERE email = % s AND password = md5(%s)', (femail, fpassword))
                admin = cur.fetchone()              
                if admin:
                    session['loggedin'] = True
                    session['id'] = admin['id']
                    session['email'] = admin['email'] 
                    flash('you sucseesfully login')                   
                    return redirect('admin_home')
                else:
                   error="username ans password are incorrect" 
                   return render_template("admin_login.html",error=error)
        return  render_template("admin_login.html")

@app.route("/admin_home")
def admin_home():
    if 'loggedin' in session:
        cur = db.connection.cursor() 
        cur.execute("select id,email,user_name,password from User_login") 
        Result=cur.fetchall()       
        return render_template('admin_home.html', Result = Result)
    else:
        error='login please'
        return render_template('admin_login.html',error=error)
    
    
    
#===========================================  CREATE USER   =====================================================
@app.route('/add_user')
def add():
    if 'loggedin' in session:
        return render_template('create_user.html')
    else:
        error='login please'
        return render_template('admin_login.html',error=error)


@app.route('/create_user',methods=['GET', 'POST'])
def create_user():
    if 'loggedin' in session:
        if request.method == 'POST':
            email =request.form.get("email")
            username=request.form.get("username")
            password=request.form.get("repassword")

            if not email or not username or not password:
                error='please fill every field'
                return render_template('create_user.html',error=error)
            elif not re.match('([A-Za-z0-9]+[.-_])*[A-Za-z0-9][email protected][A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',email):
                email='please enter valid email'
                return render_template('create_user.html',email=email)
            elif not re.match('[A-Za-z][A-Za-z0-9_]{7,29}$',username):
                username='please enter valid username'
                return render_template('create_user.html',username=username)
            elif not re.match('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}',password):
                password='please enter valid password'
                return render_template('create_user.html',password=password)
            else:

                cur = db.connection.cursor()
                cur.execute(''' INSERT INTO User_login (email,user_name,password) VALUES(%s,%s,md5(%s))''',(email,username,password))
                db.connection.commit()
                msg = Message('System Provide Username And Password for login the system', sender = 'dhruvikaneriya52@gmail.com', recipients = [email] )
                msg.body = "Username :- " + username + "\n Passeord :- " + password + "\n\n you can click on this link and login our website :-" + "http://127.0.0.1:5000/user_login"
                mail.send(msg)

                flash('user created')
                cur.execute("select id,email,user_name,password from User_login") 
                Result=cur.fetchall()
                return redirect('/admin_home')
    else:
        error='login please'
        return render_template('admin_login.html',error=error)
    

#==================================   SHOW USER IN DETAILS   =======================================================

@app.route('/showduseretails/<id>',methods=['GET', 'POST'])
def showuserdetails(id):
    if 'loggedin' in session:
        cur = db.connection.cursor()
        cur.execute('SELECT * FROM User_login WHERE id = %s', [id])
        valuse = cur.fetchall()
        print(valuse[0])
        if cur.execute('SELECT * FROM Update_Profile  WHERE user_id = %s',[id]) == 1:
            data = cur.fetchall()
            cur.execute('SELECT * FROM User_login WHERE id = %s', [id])
            values = cur.fetchall()
            print(values[0])
            cur.execute('SELECT profile_photo FROM Update_Profile WHERE user_id = %s', [id])
            img=cur.fetchone()
            filename=img.get('profile_photo')
            
            cur.execute('SELECT certificate_of_dob FROM Update_Profile WHERE user_id = %s', [id])
            pdf=cur.fetchone()
            pdfnm=pdf.get('certificate_of_dob')
            
            print(data[0])  
         
    
            return render_template('showuserdetails.html', Result=data[0],values=values[0],pdfnm=pdfnm,filename=filename)
        else:
            error='user not created there profile'
            cur.execute("select id,email,user_name,password from User_login") 
            Result=cur.fetchall()
            return render_template('admin_home.html',error=error,Result=Result)
    else:
        error='login please'
        return render_template('admin_login.html',error=error)



@app.route('/admin_update_profile/<id>',methods=['GET', 'POST'])
def admin_update_profile(id):
    if 'loggedin' in session:
    
        if request.method == 'POST':
            
            firstname =request.form.get("fname")
            lastname=request.form.get("lname")
            dob=request.form.get("bob")
            mobileno=request.form.get("mobile_no")
            gender=request.form.get("gender")
            address=request.form.get("address")
            city=request.form.get("city")
            state=request.form.get("state")
            zipcode=request.form.get("zipcode")
            updated_dt=date.today()
            cur = db.connection.cursor()
            cur.execute('SELECT * FROM Update_Profile  WHERE id = %s', [id])
            data = cur.fetchall()
            cur.execute('SELECT * FROM User_login WHERE id = %s', [id])
            values = cur.fetchall()
            print(values[0])
             
            print(data[0])   
            
            if not firstname or not lastname or not gender or not mobileno or not address or not city or not dob:
                error='please fill every field'
                return render_template('showuserdetails.html',error=error,Result=data[0],values=values[0])
            elif not re.match('[A-za-z]+',firstname):
                fname='please enter only alphabet'
                return render_template('showuserdetails.html',fname=fname,Result=data[0],values=values[0])

            elif not re.match('[A-za-z]+',lastname):
                lname='please enter only alphabet'
                return render_template('showuserdetails.html',lname=lname,Result=data[0],values=values[0])
            
            elif not re.match('[0-9]+',mobileno):
                mobileno='please enter only digit'
                return render_template('showuserdetails.html',mobileno=mobileno,Result=data[0],values=values[0])

            elif not re.match('[A-Za-z0-9\.\-\s\,]+',address):
                address='please enter only alphabet'
                return render_template('showuserdetails.html',address=address,Result=data[0],values=values[0])

            elif not re.match('[A-za-z]+',city):
                city='please enter only alphabet'
                return render_template('showuserdetails.html',city=city,Result=data[0],values=values[0])

            elif not re.match('[A-za-z]+',state):
                state='please enter only alphabet'
                return render_template('showuserdetails.html',state=state,Result=data[0],values=values[0])

            elif not re.match('[0-9]+',zipcode):
                zipcode='please enter only alphabet'
                return render_template('showuserdetails.html',zipcode=zipcode,Result=data[0],values=values[0])

            else:
                cur.execute('UPDATE Update_Profile SET first_name = %s,last_name = %s ,date_of_birth= %s ,mobile_number=%s ,gender=%s ,address=%s ,city=%s,state=%s ,zipcode=%s ,profile_updated_dt=%s WHERE id = %s', (firstname,lastname,dob,mobileno,gender,address,city,state,zipcode,updated_dt, id))
                db.connection.commit()   
                flash(' User Profile updated')
                return redirect('/admin_home')
        
        return  redirect("/admin_home")
    else:
        error='login please'
        return render_template('admin_login.html',error=error)
    

#============================================== EDIT USER PASSWORD   =============================================

@app.route('/editpassword/<id>')
def editpassword(id):
    if 'loggedin' in session:

        cur = db.connection.cursor()
        cur.execute('SELECT * FROM User_login  WHERE id = %s',[id])
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('editpassword.html', Result=data[0])
    else:
        error='login please'
        return render_template('admin_login.html',error=error)
@app.route('/updatepassword/<id>', methods=['POST', 'GET'])
def updatepassword(id):
    if 'loggedin' in session:
        if request.method == 'POST':

            newpassword = request.form['newpassword']
            repassword = request.form['repassword']
            cur = db.connection.cursor()
            cur.execute('SELECT * FROM User_login  WHERE id = %s',[id])
            data = cur.fetchall()
            cur.close()
            print(data[0])
            if not newpassword or not repassword:
                error='please fill newpassword and confirm password'
                return render_template('editpassword.html',error=error,Result=data[0])

            elif not re.match('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}',newpassword):
                email='please enter upercase,lowecase,digit and special character'
                return render_template('editpassword.html',newpassword=email,Result=data[0])

            elif not re.match('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}',repassword):
                username='please enter upercase,lowecase,digit and special character'
                return render_template('editpassword.html',repassword=username,Result=data[0])
            else:
                if newpassword==repassword:
                    cur = db.connection.cursor()
                    cur.execute('UPDATE User_login SET password = md5(%s) WHERE id = %s', (repassword, id))   
                    db.connection.commit()
                    email = request.form['email']
                    msg = Message('System Provide New Password for login the system', sender = 'dhruvikaneriya52@gmail.com', recipients = [email] )
                    msg.body = "Admin Update your Login password\n"+"\n Your New Password :- " + newpassword + "\n\n you can click on this link and login our website :-" + "http://127.0.0.1:5000/user_login"
                    mail.send(msg)
                    msg='your new password send in in your mail please check your email'
                    flash('password updated')
                    if 'loggedin' in session:
                        return redirect('/admin_home')
                else:

                    cur = db.connection.cursor()
                    cur.execute("SELECT * FROM User_login  WHERE id = %s", [id]) 
                    data = cur.fetchall()
                    cur.close()
                    print(data[id])
                    flash('New Password And Confim Password are not same')
                    return render_template('editpassword.html',Result = data[id ])
    else:
        error='login please'
        return render_template('admin_login.html',error=error)

#======================================   UPDATE USER   ============================================================

@app.route('/edit/<id>')
def get_user(id):
    if 'loggedin' in session:
        cur = db.connection.cursor()
        cur.execute('SELECT * FROM User_login  WHERE id = %s', [id])
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('edit_user.html', Result=data[0])
    else:
        flash('login please')
        return redirect('admin_login')


@app.route('/update/<id>', methods=['POST', 'GET'])
def update_user(id):
    if 'loggedin' in session:
        email = request.form['email']
        username = request.form['username']

        cur = db.connection.cursor()
        cur.execute('SELECT * FROM User_login  WHERE id = %s', [id])
        data = cur.fetchall()
        cur.close()
        print(data[0])


        if not email or not username:
            error='please fill every field'
            return render_template('edit_user.html',error=error,Result=data[0])
        elif not re.match('([A-Za-z0-9]+[.-_])*[A-Za-z0-9][email protected][A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',email):
            email='please enter valid email'
            return render_template('edit_user.html',email=email,Result=data[0])
        elif not re.match('[A-Za-z][A-Za-z0-9_]{7,29}$',username):
            username='please enter valid username'
            return render_template('edit_user.html',username=username,Result=data[0])
        else:
            cur = db.connection.cursor()
            cur.execute('UPDATE User_login SET email = %s,user_name = %s WHERE id = %s', (email, username, id))   
            db.connection.commit()
            cur.execute("select id,email,user_name from User_login") 
            cur.fetchall()
            msg = Message('System Update Username for login the system', sender = 'dhruvikaneriya52@gmail.com', recipients = [email] )
            msg.body = "New Username :- " + username + "\n\n you can click on this link and login our website :-" + "http://127.0.0.1:5000/user_login"
            mail.send(msg)
            flash('email or username updated')
           
            return redirect('/admin_home')
    else:
        flash('login please')
        return redirect('admin_login')

#============================================= Delete  ============================================================

@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_user(id):
   
    cur = db.connection.cursor()
    cur.execute('select email from User_login where id = %s',[id])
    email=cur.fetchone()
    send=email.get('email')
    
    msg = Message('System provied login information', sender = 'dhruvikaneriya52@gmail.com', recipients = [send])
    msg.body = 'You will no longer be able to login to our website because we have deleted your login records.'
    mail.send(msg)
    if cur.execute('SELECT * FROM Update_Profile WHERE user_id = %s', [id])==1:
        cur.fetchall()
        cur.execute('SELECT user_name FROM User_login WHERE id = %s', [id])
        unm = cur.fetchone()
        filename=unm.get('user_name')

        aa=filename+'.png'
        filename=aa
        
        os.remove("static/profilephoto/"+ filename)
        pdf=unm.get('user_name')
        pdfnm=pdf+'.pdf'
        os.remove("static/pdf/"+ pdfnm)
        cur.execute('DELETE FROM User_login  WHERE id = {0}'.format(id)) 
        db.connection.commit()
    else:
        cur.execute('DELETE FROM User_login  WHERE id = {0}'.format(id)) 
        db.connection.commit()

    
    flash('user deleted')
   
    return redirect('/admin_home')


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#--------------------------------  SHOW ADMIN  ------------------------------------------    
@app.route("/show_admin")
def show_admin():
    if 'loggedin' in session:
        cur = db.connection.cursor() 
        cur.execute("select id,email,password from Admin_login") 
        Result=cur.fetchall()
        return render_template('showadmin.html', Result = Result)
    else:
        flash('login please')
        return redirect('admin_login')


#--------------------------  CREATE ADMIN   ------------------------------------

@app.route('/add_admin')
def add_admin():
    if 'loggedin' in session:
        return render_template('create_admin.html')
    else:
        return redirect('admin_login')


@app.route('/create_admin',methods=['GET', 'POST'])
def create_admin():
    if 'loggedin' in session:
        if request.method == 'POST':
            email =request.form.get("email")
            password=request.form.get("repassword")
            cur = db.connection.cursor()
            cur.execute(''' INSERT INTO Admin_login (email,password) VALUES(%s,md5(%s))''',(email,password))
            db.connection.commit()
            msg = Message('System Provide Username And Password for login the system', sender = 'dhruvikaneriya52@gmail.com', recipients = [email] )
            msg.body = "\n Passeord :- " + password + "\n\n you can click on this link and login our website :-" + "http://127.0.0.1:5000/admin_login"
            mail.send(msg)
            
            flash('admin created')
        return redirect('showadmin')
    else:
        flash('login please')
        return redirect('admin_login')


#=====================   UPDATE ADMIN   ============================================================

@app.route('/edit_admin/<id>', methods=['POST', 'GET'])
def get_admin(id):
    if 'loggedin' in session:
        cur = db.connection.cursor()
        cur.execute('SELECT * FROM Admin_login  WHERE id = %s', (id))
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('edit_admin.html', Result=data[0])
    else:
        flash('login please')
        return redirect('admin_login')


@app.route('/update_admin/<id>', methods=['POST', 'GET'])
def update_admin(id):
    
        email = request.form['email']
        password = request.form['repassword']
        cur = db.connection.cursor()
        cur.execute('UPDATE Admin_login SET email = %s,password = md5(%s) WHERE id = %s', (email, password, id))   
        db.connection.commit()
        cur.execute("select id,email,password from Admin_login") 
        Result=cur.fetchall()
        msg = Message('System Update your Password for login the system', sender = 'dhruvikaneriya52@gmail.com', recipients = [email] )
        msg.body = "\n Passeord :- " + password + "\n\n you can click on this link and login our website :-" + "http://127.0.0.1:5000/user_login"
        mail.send(msg)
        flash('admin updated')
        return render_template('showadmin.html', Result = Result)

#======================================== Delete Admin ============================================================

@app.route('/delete_admin/<string:id>', methods=['POST', 'GET'])
def delete_admin(id):
   
    cur = db.connection.cursor()

    cur.execute('DELETE FROM Admin_login WHERE id = {0}'.format(id))   
    db.connection.commit()
    cur.execute("select id,email,password from Admin_login") 
    Result=cur.fetchall()
    flash('admin deleted')
    return render_template('showadmin.html', Result = Result)


#========================================== USER LOGIN ============================================================

@app.route("/user_login" ,methods=['GET', 'POST'])
def user_login():
    
    if request.method == 'POST':
        username =request.form.get("username")
        password=request.form.get("repassword")
         
        if not username or not password:
            error='must be enter username or password'
            return render_template("user_login.html",error=error)
        else:

                cur = db.connection.cursor() 
                cur.execute('SELECT * FROM User_login WHERE  user_name = % s AND password = md5(%s)', (username, password ))
                Result = cur.fetchone()
                if Result:
                    session['userloggedin'] = True
                    session['id'] = Result['id']

                    session['username'] = Result['user_name']
                    flash('login successfully!!!! \n')       
                    return redirect('userhome')            
                else:
                    error='please valid username or password'
                    return render_template("user_login.html",error=error) 
    return  render_template("user_login.html")
    

@app.route("/userhome" )
def userhome():
    if 'userloggedin' in session :
        uid=session['id']
        msg=session['username']   
        cur = db.connection.cursor() 
        cur.execute('SELECT * FROM User_login WHERE id = %s', [uid])
        valuse = cur.fetchall()
        print(valuse[0])
        if cur.execute('SELECT * FROM Update_Profile WHERE user_id = %s', [uid])==1:
            data = cur.fetchall()
            print(data[0])
            cur.execute('SELECT profile_photo FROM Update_Profile WHERE user_id = %s', [uid])
            img=cur.fetchone()
            filename=img.get('profile_photo')
            
            return render_template('user_home.html',Result=data[0],msg=msg,valuse=valuse[0],filename=filename)
        else:
            
            filename="images.png"
            flash('\n you create your ptofile right now')
            return render_template('user_home.html',Result="",filename=filename,msg=msg,valuse=valuse[0])
    else:
        flash('login please')
        return redirect('user_login')
   
    
#========================================== INSERT USER PROFILE   =============================================

@app.route("/checkedprofile")
def checkedprofile():
    if 'userloggedin' in session :
        uid=session['id']
        msg=session['username'] 
        cur = db.connection.cursor()
        if cur.execute('SELECT * FROM Update_Profile  WHERE user_id = %s', [uid])==1:  
             
            flash("you already created your profile")      
            return redirect('userhome')
        else:
            cur.execute('SELECT * FROM User_login WHERE id = %s', [uid])
            values = cur.fetchall()
            print(values[0])
            return render_template('create_user_profile.html',values=values[0])
    else:
        flash('Please Login')
        return  redirect("user_login")
    

#..................................

@app.route('/insert_user_profile')
def insert_user_profile():
    if 'userloggedin' in session : 
        return render_template("create_user_profile.html")
    else:
        flash('login please')
        return redirect('user_login')
    


@app.route('/insert_profile',methods=['GET', 'POST'])
def insert_profile():
    if 'userloggedin' in session : 
        uid=session['id'] 
        msg=session['username'] 
        if request.method == 'POST':         
            firstname =request.form.get('fname')
            lastname=request.form.get('lname')
            dob=request.form.get('bob')
            mobileno=request.form.get('mobile_no')
            gender=request.form.get('gender')
            address=request.form.get('address')
            city=request.form.get("city")
            state=request.form.get("state")
            zipcode=request.form.get("zipcode")
            file = request.files["file"]
            pdf= request.files["pdf"]
            updated_dt=date.today()
            cur = db.connection.cursor()
            cur.execute('SELECT * FROM User_login WHERE id = %s', [uid])
            values = cur.fetchall()
            print(values[0])

            if not firstname or not lastname or not dob or not mobileno or not gender or not address or not city or not state or not zipcode:
                error='please fill every field'
                return render_template('create_user_profile.html',error=error,values=values[0])

            elif not re.match('[A-za-z]+',firstname):
                fname='please enter only alphabet'
                return render_template('create_user_profile.html',fname=fname,values=values[0])

            elif not re.match('[A-za-z]+',lastname):
                lname='please enter only alphabet'
                return render_template('create_user_profile.html',lname=lname,values=values[0])

            elif not re.match('[0-9]+',mobileno):
                mobileno='please enter only digit'
                return render_template('create_user_profile.html',mobileno=mobileno,values=values[0])

            elif not re.match('[A-Za-z0-9\.\-\s\,]+',address):
                address='please enter only alphabet'
                return render_template('create_user_profile.html',address=address,values=values[0])

            elif not re.match('[A-za-z]+',city):
                city='please enter only alphabget'
            elif not re.match('[A-za-z]+',state):
                state='please enter only alphabet'
                return render_template('create_user_profile.html',state=state,values=values[0])

            elif not re.match('[0-9]+',zipcode):
                zipcode='please enter only alphabet'
                return render_template('create_user_profile.html',zipcode=zipcode,values=values[0])
            elif file.filename == '':
                img='No image selected for uploading'
                return render_template('create_user_profile.html',img=img,values=values[0])
            elif pdf == '':
                img='No image selected for uploading'
                return render_template('create_user_profile.html',img=img,values=values[0])
            else:
                filename = secure_filename(file.filename)
                pdfnm = secure_filename(pdf.filename)
                if filename.lower().endswith(('.png', '.jpg',)) and pdfnm.lower().endswith(('.pdf'))==1:

                    cur.execute('SELECT user_name FROM User_login WHERE id = %s', [uid])
                    unm = cur.fetchone()
                    filename=unm.get('user_name')
                    aa=filename+'.png'
                    filename=aa
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    pdfnm=unm.get('user_name')
                    aa=pdfnm+'.pdf'
                    pdfnm=aa
                    pdf.save(os.path.join(app.config['UPLOAD_FOLDER_A'], pdfnm))

                    cur.execute(''' INSERT INTO Update_Profile (user_id,first_name,last_name,date_of_birth,mobile_number,gender,address,city,state,zipcode,profile_updated_dt,profile_photo,certificate_of_dob)
                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(uid,firstname,lastname,dob,mobileno,gender,address,city,state,zipcode,updated_dt,filename,pdfnm))
                    db.connection.commit()

                    cur.execute('SELECT * FROM Update_Profile WHERE  user_id = %s ', [uid] )
                    data=cur.fetchall()
                    print(data)

                    cur.execute('SELECT * FROM User_login WHERE id = %s', [uid])
                    valuse = cur.fetchall()
                    print(valuse[0])

                    flash('Your Profile is created')
                    return render_template('user_home.html',msg=msg,Result=data[0],valuse=valuse[0],filename=filename,pdf=pdf)
                else:
                
                    flash('use file estension .png and .jpg')
        else:
            return redirect('insert_user_profile')

    else:
        flash('login please')
        return redirect('user_login')

@app.route('/display/<filename>')
def display_image(filename):
    
    return redirect(url_for('static', filename='profilephoto/' + filename))

@app.route('/display_pdf')
def display_pdf():
    uid=session['id'] 
    cur = db.connection.cursor()
    cur.execute('SELECT certificate_of_dob FROM Update_Profile WHERE  user_id = %s ', [uid] )
    pdf=cur.fetchone()
    pdfnm=pdf.get('certificate_of_dob')
    return redirect(url_for('static', filename='pdf/' + pdfnm))

@app.route('/display_pdf_admin/<pdfnm>')
def display_pdf_admin(pdfnm):
   
    return redirect(url_for('static', filename='pdf/' + pdfnm))


#===================== EDIT AND SHOW USER PROFILE   =============================================
@app.route('/editprofile/',methods=['GET', 'POST'])
def editprofile():
    if 'userloggedin' in session :
        uid=session['id']
        msg=session['username']
        cur = db.connection.cursor()
        
        if cur.execute('SELECT * FROM Update_Profile  WHERE user_id = %s', [uid])==1:
            data = cur.fetchall()
            cur.execute('SELECT * FROM User_login WHERE id = %s', [uid])
            valuse = cur.fetchall()
            print(valuse[0])
            cur.close()   
            print(data[0])        
            return render_template('edit_profile.html', Result=data[0],valuse=valuse[0])
        else:
            cur.execute('SELECT * FROM Update_Profile WHERE  user_id = %s ', [uid] )
            data=cur.fetchall()
            print(data)
        
            cur.execute('SELECT * FROM User_login WHERE id = %s', [uid])
            valuse = cur.fetchall()
            print(valuse[0])
            cur.close()
            flash('you not create your profile')
            return redirect('userhome')
    else:
        flash('login pleasse')
        return redirect('user_login')
        
   
    

@app.route('/update_profile',methods=['GET', 'POST'])
def update_profile():
    
    if 'userloggedin' in session :
        uid=session['id']
        if request.method == 'POST':
           
            firstname =request.form.get("fname")
            lastname=request.form.get("lname")
            dob=request.form.get("birthdt")
            mobileno=request.form.get("mobile_no")
            gender=request.form.get("gender")
            address=request.form.get("address")
            city=request.form.get("city")
            state=request.form.get("state")
            zipcode=request.form.get("zipcode")
            file = request.files["file"]
            pdf= request.files["pdf"]
            updated_dt=date.today()
            cur = db.connection.cursor()
            cur.execute('SELECT * FROM User_login WHERE id = %s', [uid])
            valuse = cur.fetchall()
            print(valuse[0])
            cur = db.connection.cursor()
            cur.execute('SELECT * FROM Update_Profile  WHERE user_id = %s', [uid])
            data = cur.fetchall()
            filename = secure_filename(file.filename)
            pdfnm = secure_filename(pdf.filename) 
            print(data[0])   

            if not firstname or not lastname or not dob or not mobileno or not gender or not address or not city or not state or not zipcode:
                error='please fill every field'
                return render_template('edit_profile.html',error=error,Result=data[0],valuse=valuse[0])
            elif not re.match('[A-za-z]+',firstname):
                fname='please enter only alphabet'
                return render_template('edit_profile.html',fname=fname,Result=data[0],valuse=valuse[0])

            elif not re.match('[A-za-z]+',lastname):
                lname='please enter only alphabet'
                return render_template('edit_profile.html',lname=lname,Result=data[0],valuse=valuse[0])
            
            elif not re.match('[0-9]+',mobileno):
                mobileno='please enter only alphabet'
                return render_template('edit_profile.html',mobileno=mobileno,Result=data[0],valuse=valuse[0])

            elif not re.match('[A-Za-z0-9\.\-\s\,]+',address):
                address='please enter only alphabet'
                return render_template('edit_profile.html',address=address,Result=data[0],valuse=valuse[0])

            elif not re.match('[A-za-z]+',city):
                city='please enter only alphabet'
                return render_template('edit_profile.html',city=city,Result=data[0],valuse=valuse[0])

            elif not re.match('[A-za-z]+',state):
                state='please enter only alphabet'
                return render_template('edit_profile.html',state=state,Result=data[0],valuse=valuse[0])

            elif not re.match('[0-9]+',zipcode):
                zipcode='please enter only alphabet'
                return render_template('edit_profile.html',zipcode=zipcode,Result=data[0],valuse=valuse[0])
            
                
                
               
            else:
               
                if filename.lower().endswith(('.png', '.jpg',)) and   pdfnm.lower().endswith(('.pdf'))==1:
                    cur.execute('SELECT user_name FROM User_login WHERE id = %s', [uid])
                    unm = cur.fetchone()
                    filename=unm.get('user_name')
                    aa=filename+'.png'
                    filename=aa
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    pdfnm=unm.get('user_name')
                    aa=pdfnm+'.pdf'
                    pdfnm=aa
                    pdf.save(os.path.join(app.config['UPLOAD_FOLDER_A'], pdfnm))

                    cur.execute('UPDATE Update_Profile SET first_name = %s,last_name = %s ,date_of_birth= %s ,mobile_number=%s ,gender=%s ,address=%s ,city=%s,state=%s ,zipcode=%s ,profile_updated_dt=%s WHERE user_id = %s', (firstname,lastname,dob,mobileno,gender,address,city,state,zipcode,updated_dt, uid))
                    db.connection.commit()
                    cur.execute('UPDATE Update_Profile SET profile_photo=%s,certificate_of_dob=%s WHERE id = %s', (filename,pdfnm, uid))
                    db.connection.commit()
                    flash('You Update Your Profile')   
                    return redirect('userhome')
                else:
                    flash('asgfresdjyghufjkiygujtki8ogtrgterdhysgtfehyrd')
        return redirect('editprofile')           
    else:   
        flash("Please Login")
        return  redirect("user_login")
    
    
    
#===================== USER RESET THERE PASSWORD   =============================================
@app.route('/email',methods=['POST', 'GET'])
def email():    
    return render_template('email.html')

@app.route('/sendmail',methods=['POST', 'GET'])
def sendmail():
    email=request.form['email']
    cur = db.connection.cursor()
    if cur.execute('select id from User_login where email = %s',[email])==1:
        id=cur.fetchone()
        send=id.get('id')
        uid=str(send)
        msg = Message('Reset Your Password', sender = 'dhruvikaneriya52@gmail.com', recipients = [email] )
        msg.body = "\n\n you can click on this link and reset your password :-" + "http://127.0.0.1:5000/updateuserpassword/"+uid
        mail.send(msg)
        flash('if you can reset your password  then you check your mail right now')
        return redirect('email')
    else:
        flash('You can not change password becuse you not exist our site')
        return redirect('user_login')

        


@app.route('/updateuserpassword/<int:id>', methods=['POST', 'GET'])
def updateusetpassword(id):
   
    
    if request.method == 'POST':
        email=request.form['email']  
        newpassword = request.form['newpassword']
        repassword = request.form['repassword']
        cur = db.connection.cursor()
        cur.execute('SELECT id FROM User_login  WHERE id = %s',[id])
        data = cur.fetchall()
        cur.close()
        print(data[0])
        if not newpassword or not repassword:
            error='please fill newpassword and confirm password'
            return render_template('resetpasseord.html',error=error,Result=data[0])

        elif not re.match('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}',newpassword):
            email='please enter upercase,lowecase,digit and special character'
            return render_template('resetpasseord.html',newpassword=email,Result=data[0])

        elif not re.match('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}',repassword):
            username='please enter upercase,lowecase,digit and special character'
            return render_template('resetpasseord.html',repassword=username,Result=data[0])
        else:
            if newpassword==repassword:
                cur = db.connection.cursor()
                if cur.execute('UPDATE User_login SET password = md5(%s) WHERE id = %s', (newpassword, id))==1:   
                    db.connection.commit()
                    cur.execute("select id,email,user_name,password from User_login")  
                    cur.fetchall()
                    msg = Message('System Provide Username And Password for login the system', sender = 'dhruvikaneriya52@gmail.com', recipients = [email] )
                    msg.body = "\n Your Password :- " + newpassword + "\n\n you can click on this link and login our website :-" + "http://127.0.0.1:5000/user_login"
                    mail.send(msg)
                    msg='your new password send in in your mail please check your email'

   
                    return render_template('user_login.html',msg=msg)
            else:


                cur = db.connection.cursor()
                cur.execute("SELECT * FROM User_login  WHERE id = %s", [id] ) 
                data = cur.fetchall()
                cur.close()
                print(data[id])
                flash('New Password And Confim Password are not same')
                return render_template('resetpasseord.html',Result = data[id])
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM User_login WHERE id = %s",[id]) 
    data = cur.fetchall()
    print(data[0])
    flash('Now you set your new password')
    return render_template('resetpasseord.html',Result = data[0])

#=============================== SIGN UP USER   =============================================
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email =request.form.get("email")
        username=request.form.get("username")
        password=request.form.get("repassword")

        if not email or not username or not password:
            error='please fill every field'
            return render_template('sign_up.html',error=error)
        elif not re.match('([A-Za-z0-9]+[.-_])*[A-Za-z0-9][email protected][A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+',email):
            email='please enter valid email'
            return render_template('sign_up.html',email=email)
        elif not re.match('[A-Za-z][A-Za-z0-9_]{7,29}$',username):
            username='please enter valid username'
            return render_template('sign_up.html',username=username)
        elif not re.match('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}',password):
            password='please enter valid password'
            return render_template('sign_up.html',password=password)
        else:
            
            cur = db.connection.cursor()
            if cur.execute('SELECT email FROM User_login WHERE  email=%s', [email])==1:
                flash('you can not sign up our site becuse you already exist')
                return redirect('user_login')
            else:
                
                cur.execute(''' INSERT INTO User_login (email,user_name,password) VALUES(%s,%s,md5(%s))''',(email,username,password))
                db.connection.commit()
                msg = Message('Username and passeord for system login', sender = 'dhruvikaneriya52@gmail.com', recipients = [email] )
                msg.body = "Username :- " + username + "\n Passeord :- " + password + "\n\n you can click on this link and login our website :-" + "http://127.0.0.1:5000/user_login"
                mail.send(msg)
                cur = db.connection.cursor() 
                cur.execute('SELECT * FROM User_login WHERE  user_name = % s AND password = md5(%s)', (username, password ))
                Result = cur.fetchone()

                if Result:
                    session['userloggedin'] = True
                    session['id'] = Result['id']

                    session['username'] = Result['user_name']

                    return redirect('userhome') 
    else:
        flash('noy sing up')
        return redirect()
           

if __name__ == "__main__":
  app.run(debug=True)