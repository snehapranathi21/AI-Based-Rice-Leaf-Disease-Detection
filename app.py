from flask import Flask,render_template,session,flash,redirect,request,send_from_directory,url_for
import mysql.connector, os
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from datetime import datetime
import time
app=Flask(__name__)
app.config['SECRET_KEY']='attendance system'

def data_bace():
    db = mysql.connector.connect(host="localhost", user="root", passwd="", database="rice_crop_leaf")
    cur=db.cursor()
    return db,cur


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signin', methods=['POST','GET'])
def signin():
    if request.method=='POST':
        useremail = request.form['userEmail'] 
        password = request.form['userPassword']

        db,cur=data_bace()
        sql="select * from users where user_Email='"+useremail+"' and Password='"+password+"'"
        cur.execute(sql)
        data=cur.fetchall()
        user_type=data[0][1]
        print(user_type)
        db.commit()
        if data==[]:
            flash("Invalid data entered","danger")
            return render_template('signin.html')
        else:
            if user_type=="Farmer":
                session['useremail']=useremail
                session['username']=data[0][2]
                flash("welcome ","success")
                return render_template('userdash.html')
            else:
                session['useremail']=useremail
                session['username']=data[0][2]
                flash("welcome ","success")
                return redirect(url_for('farmer_request'))
    return render_template('signin.html')

@app.route('/contact',methods=["POST","GET"])
def contact():
    if request.method=='POST':
        usertype=request.form['userType']
        username=request.form['userName']
        useremail = request.form['userEmail']       
        password = request.form['userPassword']
        mobile = request.form['userPhone']
        address = request.form['userAddr']
        db,cur=data_bace()
        sql="select * from users where user_Email='%s' "%(useremail)
        cur.execute(sql)
        data=cur.fetchall()
        db.commit()
        if data==[]:
            sql = "insert into users(user_Type,user_Name,user_Email,Password,user_Phone,user_Addr) values(%s,%s,%s,%s,%s,%s)"
            val=(usertype,username,useremail,password,mobile,address)
            cur.execute(sql,val)
            db.commit()
            flash("User registered Successfully","success")
            return render_template("contact.html")
        else:
            flash("Details already Exists","warning")
            return render_template("contact.html")
        
    return render_template('contact.html')

@app.route('/userdash')
def userdash():
    return render_template('userdash.html')

@app.route("/upload", methods=["POST","GET"])
def upload():
    print('a')
    if request.method=='POST':
        myfile=request.files['file']
        fn=myfile.filename
        mypath=os.path.join('images/', fn)
        myfile.save(mypath)
        accepted_formated=['jpg','png','jpeg','jfif','JPG']
        if fn.split('.')[-1] not in accepted_formated:
            flash("Image formats only Accepted","Danger")
            return render_template("upload.html")
        new_model = load_model(r"models/mobilenet.h5")
        test_image = image.load_img(mypath, target_size=(256, 256))

        test_image = image.img_to_array(test_image)
        test_image = test_image/255
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)
        print(result)
        print(np.argmax(result))
        classes=['Bacterial_leaf_blight', 'Brown_spot', 'Healthy', 'Leaf_blast', 'Leaf_scald', 'Narrow_brown_spot']
        prediction=classes[np.argmax(result)]
        if prediction=="Bacterial_leaf_blight":
            msg="Bacterial Leaf Blight: Caused by the bacterium Xanthomonas oryzae pv. oryzae. This bacterium infects the rice plant through wounds or natural openings (like stomata), often favored by wet conditions. It leads to symptoms like wilting, yellowing, and drying of leaves."
        elif prediction=="Brown_spot":
            msg="Brown Spot: Triggered by the fungus Cochliobolus miyabeanus (formerly known as Helminthosporium oryzae). This disease is common in nutrient-deficient soils, especially where there is a deficiency of silicon and nitrogen. It's characterized by brown spots on leaves and can severely affect seed quality and yield." 
        elif prediction=="Healthy":
            msg="Healthy: This is not a disease but rather the desired state of the plant. Maintaining plant health involves proper agricultural practices, including appropriate watering, fertilization, and disease control measures."
        elif prediction=="Leaf_blast":
            msg="Leaf Blast: Caused by the fungus Pyricularia grisea, also known as Magnaporthe grisea. The disease thrives in conditions of high humidity and moderate temperatures and is characterized by diamond-shaped or eye-shaped spots on the leaves. It can cause significant crop losses."
        elif prediction=="Leaf_scald":
            msg="Leaf Scald: This disease is caused by the bacterium Xanthomonas oryzae pv. oryzicola. It's less destructive than bacterial leaf blight but still causes considerable damage. Symptoms include long, narrow, pale green to grayish water-soaked streaks on leaves."
        else:
            msg="Narrow Brown Spot: This is caused by the fungus Cercospora janseana. It's a minor disease that appears as narrow, brown, linear lesions on the leaf blades. The disease is more common in older leaves and in fields with high nitrogen levels."

        return render_template("result.html",image_name=fn, text=prediction, msg=msg)
    return render_template('upload.html')
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


if __name__=='__main__':
    app.run(debug=True)