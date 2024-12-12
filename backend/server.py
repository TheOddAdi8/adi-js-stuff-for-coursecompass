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
    # Connecting to the server
    dataBase = connectToData()

    # preparing a cursor object
    cursor = dataBase.cursor()
    cursor.execute("SELECT * FROM subject")
    return cursor.fetchall()

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
        statement = "SELECT * FROM CourseInfo"
        original = statement

        # Getting the school id from the division table based on the division name
        if school != "":
            print(school)
            statementTeacher = "SELECT divisionID FROM division WHERE divisionName='" + school + "'"
            cursor.execute(statementTeacher)
            schoolId = cursor.fetchall()[0][0]
            print(schoolId)
            if statement == original:
                statement+=" WHERE "
            if "=" in statement:
                statement += " AND "
            statement+="divisionID='" + str(schoolId) + "'"

        # Getting the subject id from the Subjects table
        if department != "":
            print(department)
            statementDepartment = "SELECT subjectId FROM subject WHERE subjectName='" + department + "'"
            cursor.execute(statementDepartment)
            subjectId = cursor.fetchall()[0][0]
            print(subjectId)
            if statement == original:
                statement+=" WHERE "
            if "=" in statement:
                statement += " AND "
            statement+= "subjectID='" + str(subjectId) + "'"

        # Getting the courses from the course info table based on the course name
        if course != "":
            print(course)
            if statement == original:
                statement+=" WHERE "
            if "=" in statement:
                statement += " AND "
            statement+="courseName='" + str(course) + "'"

        # Getting the teacher id from the teacherName table based on the teacher name
        teacherCourses = []
        if teacher != "":
            print(teacher)
            statementTeacher = "SELECT userID FROM teacherName WHERE teacherName='" + teacher + "'"
            cursor.execute(statementTeacher)
            teacherId = cursor.fetchall()[0][0]
            statementTeacher = "SELECT courseID FROM courseTeacher WHERE userID='" + str(teacherId) + "'"
            cursor.execute(statementTeacher)
            for i in cursor.fetchall():
                teacherCourses.append(str(i[0]))

            if statement == original:
                statement+=" WHERE "
            if "=" in statement:
                statement += " AND "
            statement+="courseID IN ("
            for i in teacherCourses:
                statement+= i+", "
            print(statement)
            statement = statement[:-2]
            statement+=")"
            
        print(statement)
        cursor.execute(statement)
        results = cursor.fetchall()

    except:
        print("Error Getting Results")

    # Formatting the course name and course ids into a string
    strResults = "No Results "
    for i in results:
        strResults += i[1] + ":" + str(i[0]) + ","
    strResults = strResults[0:len(strResults)-1]
    
    print(strResults)

    return {
        'Result':strResults
    }

@app.route('/populate')
def populate():
    # Connecting to the server
    dataBase = connectToData()

    # preparing a cursor object
    cursor = dataBase.cursor()
    statement = "SELECT divisionName FROM division"
    cursor.execute(statement)
    divisions = []
    for x in cursor.fetchall():
        divisions.append(x[0].replace("'", ""))

    statement = "SELECT subjectName FROM subject"
    cursor.execute(statement)
    subjects = []
    for x in cursor.fetchall():
        subjects.append(x[0].replace("'", ""))

    statement = "SELECT courseName FROM CourseInfo"
    cursor.execute(statement)
    courses = []
    for x in cursor.fetchall():
        courses.append(x[0].replace("'", ""))

    statement = "SELECT teacherName FROM teacherName"
    cursor.execute(statement)
    teachers = []
    for x in cursor.fetchall():
        teachers.append(x[0].replace("'", ""))
        
    return {
        'Divisions':divisions, 
        'Subjects':subjects,
        'Courses':courses,
        'Teachers':teachers
    }



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)