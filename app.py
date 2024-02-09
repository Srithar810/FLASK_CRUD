from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL

app=Flask(__name__)

#mysql Homepage
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="flask_crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql=MySQL(app)

#loading Home page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="select * from tbl_basic1"
    con.execute(sql)
    res=con.fetchall()
    return render_template ("home.html",datas=res)

#User New User
@app.route("/addUsers",methods=["GET","POST"])
def addUsers():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        con=mysql.connection.cursor()
        sql="insert into tbl_basic1 (name,age,city) values (%s,%s,%s)"
        con.execute(sql,[name,age,city])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("addUsers.html")

#Update User
@app.route("/editUser/<string:id>",methods=['GET','POST'])
def editUser(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        sql="update tbl_basic1 set name=%s,age=%s,city=%s  where id=%s"
        con.execute(sql,[name,age,city,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
    sql="select * from tbl_basic1 where id=%s"
    con.execute(sql,id)
    res=con.fetchone()
    return render_template("editUser.html",datas=res)
    
 #Delete User
@app.route("/deleteUser/<string:id>",methods=['GET','POST'])
def deleteUser(id):
    con=mysql.connection.cursor()
    sql="delete from tbl_basic1 where id=%s"
    con.execute(sql,id)
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))
 

if(__name__=='__main__'):
    app.run(debug=True)