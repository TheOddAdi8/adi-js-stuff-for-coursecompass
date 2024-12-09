from flask import Flask, request, jsonify
import mysql.connector


app = Flask(__name__)

def connectToData():
    dataBase = mysql.connector.connect(
        host="sql5.freemysqlhosting.net",
        user="sql5744928",
        passwd="wCBdQqsKCG",
        database="sql5744928"
    )
    return dataBase

@app.route('/')
def pythonHome():
    return "This is the python server"

@app.route('/data')
def showName():
    # Connecting to the server
    dataBase = connectToData()

    # preparing a cursor object
    cursor = dataBase.cursor()

    # Use dataBase.commit() when creating tables or inserting into tables
    cursor.execute("""SELECT courseName FROM CourseInfo""")
    result = cursor.fetchone()
    name = result
    cursor.fetchall()
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
    dataBase = connectToData()
    results = []
    try:
        # preparing a cursor object
        cursor = dataBase.cursor()
        # Prepares the initial sql query
        statement = "SELECT courseId FROM courseTeacher"
        # Getting the teacher id from the teacherName table based on the teacher name
        if teacher != "":
            statementTeacher = "SELECT userID FROM teacherName WHERE teacherName='" + teacher + "'"
            cursor.execute(statementTeacher)
            teacherId = cursor.fetchall()[0][0]
            if statement == "SELECT courseId FROM courseTeacher":
                statement+=" WHERE "
            if "=" in statement:
                statement += " AND "
            statement+="userID='" + str(teacherId) + "'"
        # Getting the subject id from the Subjects table
        if department != "":
            statementDepartment = "SELECT subjectId FROM subjects WHERE subjectName='" + department + "'"
            cursor.execute(statementDepartment)
            subjectId = cursor.fetchall()[0][0]
            if statement == "SELECT courseId FROM courseTeacher":
                statement+=" WHERE "
            if "WHERE" in statement:
                statement += " AND "
            statement+= "subjectID='" + str(subjectId) + "'"
        cursor.execute(statement)
        courseIds = cursor.fetchall()
        # Iterating through all the courses taught by the teacher and getting all of the data about each course from the courseInfo table
        for id in courseIds:
            id = id[0]
            statement = "SELECT * FROM CourseInfo WHERE courseId='" + str(id) + "'"
            cursor.execute(statement)
            results.append(cursor.fetchall()[0])
        
        dataBase.close()
    except:
        print("Error Getting Results")
    

    # Formatting the course name and course ids into a string
    strResults = ""
    for i in results:
        strResults += i[1] + ":" + str(i[0]) + ","
    strResults = strResults[0:len(strResults)-1]
    
    print(strResults)
    return {
        'Result':strResults
    }



if __name__ == '__main__':
    app.run(debug=True)