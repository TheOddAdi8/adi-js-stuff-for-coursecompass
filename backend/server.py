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
    cursor.execute("""SELECT courseName FROM CourseInfo""")
    result = cursor.fetchone()
    name = result
    cursor.reset()
    cursor.execute("""SELECT teacherName FROM teacherName""")
    result = cursor.fetchone()
    teacher = result

    # Disconnecting from the server
    dataBase.close()

    return {
        'Name':name,
        'Phrase':teacher
    }

# Used to search the database with inputs from the browse page
@app.route('/search', methods=['POST'])
def search():
    data = request.form['data'].replace("\"", "").split(",")
    # Process the received data
    # School, Department, Course, teacher
    school = data[0]
    department = data[1]
    course = data[2]
    teacher = data[3]
    dataBase = mysql.connector.connect(
        host="sql5.freemysqlhosting.net",
        user="sql5744928",
        passwd="wCBdQqsKCG",
        database="sql5744928"
    )
    # preparing a cursor object
    cursor = dataBase.cursor()
    # Getting the teacher id from the teacherName table based on the teacher name
    statement = "SELECT userID FROM teacherName WHERE teacherName='" + teacher + "'"
    cursor.execute(statement)
    teacherId = cursor.fetchone()[0]
    # Getting all the course ids from the courseTeacher table based on the teacher id
    statement = "SELECT courseId FROM courseTeacher WHERE userID='" + str(teacherId) + "'"
    cursor.execute(statement)
    courseIds = cursor.fetchall()
    results = []
    # Iterating through all the courses taught by the teacher and getting all of the data about each course from the courseInfo table
    for id in courseIds:
        id = id[0]
        statement = "SELECT * FROM CourseInfo WHERE courseId='" + str(id) + "'"
        cursor.execute(statement)
        results.append(cursor.fetchone())
    
    dataBase.close()

    # Formatting the course name and course ids into a string
    strResults = ""
    for i in results:
        strResults += i[1] + ":" + str(i[0]) + ","
    strResults = strResults[0:len(strResults)-1]
    
    print(strResults)
    return strResults



if __name__ == '__main__':
    app.run(debug=True)