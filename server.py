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
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    grade = request.form['grade']

    sql = "INSERT INTO students  values (%s,%s,%s,%s) "
    cursor.execute(sql,(name,age,gender,grade))
    connection.commit()

    return jsonify("create successfully !")






if __name__ =="__main__":
    app.run(debug=True)


