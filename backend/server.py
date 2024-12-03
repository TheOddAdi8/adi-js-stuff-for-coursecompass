from flask import Flask, request, jsonify
import mysql.connector


app = Flask(__name__)

@app.route('/')
def pythonHome():
    return "This is the python server"

@app.route('/data')
def showName():
    # Connecting to the server
    dataBase = mysql.connector.connect(
        host="sql5.freemysqlhosting.net",
        user="sql5744928",
        passwd="wCBdQqsKCG",
        database="sql5744928"
    )
    # preparing a cursor object
    cursor = dataBase.cursor()
    # Use dataBase.commit() when creating tables or inserting into tables
    cursor.execute("""SELECT * FROM CourseInfo""")
    result = cursor.fetchone()
    name = result[1]
    cursor.execute("""SELECT * FROM teacherName""")
    result = cursor.fetchone()
    teacher = result[1]

    # Disconnecting from the server
    dataBase.close()

    return {
        'Name':name,
        'Phrase':teacher
    }

@app.route('/search', methods=['POST'])
def search():
    data = request.form['data'].replace("\"", "").split(",")
    # Process the received data
    print(data)
    return "Data Received"


if __name__ == '__main__':
    app.run(debug=True)