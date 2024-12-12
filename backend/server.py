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
# Creates a connection to the database
def connectToData():
    dataBase = mysql.connector.connect(
        host="sql5.freemysqlhosting.net",
        user="sql5744928",
        passwd="wCBdQqsKCG",
        database="sql5744928"
    )
    return dataBase

# Homepage for the python server
# @app.route('/')
# def pythonHome():
#     return "Python Server"

# Used for the Data Testing page to display the first teacher and course in the database
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

# Used to populate the dropdown menus on the browse page
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

# Used for the edit course page to edit the courses
@app.route("/editCourse", methods=['POST'])
def editCourse():
    return "Nothing here yet"

# Used for adding a course
@app.route("/")
def addCourse():
    # textFields = request.form['data'].split(",")
    # name = textFields[0]
    # year = textFields[1]
    # grades = textFields[2]
    # subject = textFields[3]
    # division = textFields[4]
    # teacher = textFields[5]
    # units = textFields[6].split(",")
    name = "Computer Science 3"
    year = "2024"
    grades = "grades 10-12"
    subject = "English"
    division = "Upper"
    teacher = "Marcus Twyford"
    units = ["1", "2", "3"]

    # Connecting to the server
    dataBase = connectToData()

    # preparing a cursor object
    cursor = dataBase.cursor()
    # Add a new subject if the subject does not exist
    cursor.execute("SELECT subjectID FROM subject WHERE subjectName='%s'" % subject)
    if len(cursor.fetchall()) == 0:
        cursor.execute("INSERT INTO subject (subjectName) VALUES ('%s')" % subject)
    
    # Add a new division if that division does not exist
    cursor.execute("SELECT divisionID FROM division WHERE divisionName='%s'" % division)
    if len(cursor.fetchall()) == 0:
        cursor.execute("INSERT INTO subject VALUES ('%s')" % division)

    cursor.execute("SELECT subjectID FROM subject WHERE subjectName='%s'" % subject)
    subId = int(cursor.fetchone()[0])
    cursor.fetchall()
    cursor.execute("SELECT divisionID FROM division WHERE divisionName='%s'" % division)
    divId = int(cursor.fetchone()[0])
    cursor.fetchall()

    # Add to the courseInfo table
    statement = "INSERT INTO CourseInfo (courseName, subjectID, year, grade, divisionID) VALUES ('%s', %i, %i, '%s', %i)" % (name, subId, int(year), grades, divId)
    cursor.execute(statement)

    cursor.execute("SELECT @@IDENTITY")
    courseId = int(cursor.fetchall()[0][0])

    # Add to the teacher table
    cursor.execute("SELECT userID FROM teacherName WHERE teacherName='%s'" % teacher)
    if len(cursor.fetchall()) == 0:
        statement = "INSERT INTO teacherName VALUES ('%s')" % (teacher)
        cursor.execute(statement)
        cursor.execute("SELECT SCOPE_IDENTITY()")
        teacherId = cursor.fetchall()[0]
    else:
        cursor.execute("SELECT userID FROM teacherName WHERE teacherName='%s'" % teacher)
        teacherId = int(cursor.fetchall()[0][0])
    # Add to the courseTeacher table
    statement = "INSERT INTO courseTeacher VALUES (%i, %i)" % (courseId, teacherId)
    cursor.execute(statement)
    '''
    INSERT INTO unitText VALUES (1, 1, 'We want to promote diversity and inclusion in CS.');
    '''

if __name__ == '__main__':
    app.run(debug=True)