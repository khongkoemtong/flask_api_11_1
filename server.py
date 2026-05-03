from flask import Flask,jsonify,request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


def connect_db ():
    connection = psycopg2.connect(
        host="localhost",
        user = "postgres",
        database = "python_flask",
        password ="123",
        port = "5432" 
    )

    return connection


connect_db()


@app.route('/read')
def hello():
    conection = connect_db()
    cursor = conection.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM students ")

    student = cursor.fetchall()


    return jsonify(student)


@app.route('/insert' ,methods=["POST"])
def insert ():
    connection = connect_db()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    id= request.form['id']
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    grade = request.form['grade']

    sql = "INSERT INTO students  values (%s,%s,%s,%s,%s) "
    cursor.execute(sql,(id,name,age,gender,grade))
    connection.commit()

    return jsonify("create successfully !")

@app.route('/show' ,methods=["POST"])
def show ():
    conection = connect_db()
    cusor = conection.cursor(cursor_factory=RealDictCursor)
    id = request.form['id']

    sql = "SELECT * FROM students WHERE id = %s"

    cusor.execute(sql,(id,))
    student = cusor.fetchone()
    conection.commit()

    return jsonify(student)


@app.route('/update/<int:myid>',methods=['POST'])
def update (myid):
    conection = connect_db()
    cursor = conection.cursor(cursor_factory=RealDictCursor)

    id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    grade = request.form['grade']


    sql = "UPDATE students SET id =%s ,name=%s,age=%s,gender=%s ,grade=%s WHERE id = %s"
    
    cursor.execute(sql,(id,name,age,gender,grade,myid))
    conection.commit()

    return jsonify("update success !")









if __name__ =="__main__":
    app.run(debug=True)


