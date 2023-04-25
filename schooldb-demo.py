import mysql.connector

students = mysql.connector.connect(host="localhost",user="root",password="Ysfsql!03", database="schooldb")

class Student():
    connection = students
    cursor = students.cursor()

    def __init__(self, id, studentNumber, name, surname, birtdate, gender):
        if id is None:
            self.id=0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birtdate = birtdate
        self.gender = gender
    
    def saveStudent(self):  #tek kayıt eklenir
        sql = "insert into students (studentNumber, name, surname, birthdate, gender) values (%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name, self.surname, self.birtdate, self.gender)
        Student.cursor.execute(sql,value)

        try:
            students.commit()
            print(Student.cursor.rowcount,"tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            students.close()
    
    @staticmethod
    def saveStudents(liste):  #çoklu kayıt eklenir
        sql = "insert into students (studentNumber, name, surname, birthdate, gender) values (%s,%s,%s,%s,%s)"
        values = students
        Student.cursor.executemany(sql,values)

        try:
            students.commit()
            print(Student.cursor.rowcount,"tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            students.close()
    @staticmethod
    def StudentInfo():
       
        #sql = "select * from students"
        #sql = "select studentnumber,name, surname from students"
        #sql = "select name, surname from students where gender = 'K'"
        #sql = "select * from  students where birthdate=2003" 
        sql = "select name,surname from students where name or surname like '%an%'"
        sql = "select count(*) from students where gender='E'"
        sql = "select * from students where gender='K' order by name asc"
        sql = "select * from students where year(birthdate) =2003"
        sql = "select * from students where name='Ali' and year(birthdate)=2005"
        Student.cursor.execute(sql)

        result = Student.cursor.fetchall()

        for i in result:
            print(i)
        try:
            students.commit()
        except mysql.connector.Error as err:
            print("hata", err)
        finally:
            students.close()

    @staticmethod
    def getStudentById(id):
        sql = "select * from students where id=%s"
        value = (id,)
        Student.cursor.execute(sql, value)

       
        try:
            std = Student.cursor.fetchone()
            return Student(std[0],std[1],std[2],std[3],std[4],std[5])
        except mysql.connector.Error as err:
            print("hata", err)
    

    def updateStudent(self):
        sql = "update students set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birtdate,self.gender,self.id)
        Student.cursor.execute(sql,values)

        try:
            students.commit()
            print(Student.cursor.rowcount,"tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("hata", err)
    
    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from students where gender=%s"
        value = (gender,)
        Student.cursor.execute(sql,value)

        try:
            return Student.cursor.fetchall()
        except mysql.connector.Error as err:
            print("hata", err)
        
        
# Student.getStudentById(3)

# std = Student.getStudentById(3)

# std.name = "Kemal"
# std.surname = "Yaşar"
# std.updateStudent()

std = Student.getStudentsGender('E')
print(std)