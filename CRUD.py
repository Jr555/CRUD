def main():
    import pymysql
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='data',
        )
    def create():
        name = input("Enter Name: ")
        schoolA = input("Enter School Attended:  ")
        last = input("Enter Last School Attended: ")

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO crud (`Name`, `SchoolAttended`, `LastSchoolAttended`) VALUES (%s, %s, %s )"
                try:
                    cursor.execute(sql, (name, schoolA, last))
                    print("Task added successfully")
                except Exception as e:
                    print("Oops! Something wrong")
                    print (e);
     
                connection.commit()
        finally:
                connection.close()

    def read():
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM crud "
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()
     
                    print("Code\t\t Name\t\tSchool Attended\t\tLast School Attended")
                    for row in result:
                        print(str(row[0]) + "\t\t" + row[1] + "\t\t\t" + row[2] + "\t\t\t" + str(row[3]))
     
                except Exception as e:
                    print("Oops! Something wrong")
                    print (e)
     
                connection.commit()
        finally:
            connection.close()

    def update():
        
        studid=input("Input Code: ")
        print("Update\n1. Name\n2. School Attended\n3. Last School Attended\n")
        choice=int(input())

        if choice==1:
            new=input("Enter New Name:  ")
            sql = "UPDATE crud SET Name=%s WHERE `Code` = %s"
        elif choice==2:
            new=input("Enter School Attended:  ")
            sql = "UPDATE crud SET SchoolAttended=%s WHERE `Code` = %s"
        elif choice==3:
            new=input("Enter Last School Attended:  ")
            sql = "UPDATE crud SET LastSchoolAttended=%s WHERE `Code` = %s"
        else:
            print("Invalid Input")



        try:
            with connection.cursor() as cursor:
                
                try:
                    cursor.execute(sql, (new,studid))
                    print("Successfully Updated...")
                except Exception as e:
                    print("Oops! Something wrong")
                    print (e)
         
            connection.commit()
        finally:
            connection.close()
    def delete():
        id=input("Input Code  to be Deleted: ")

        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM crud WHERE Code = %s"
                try:
                    cursor.execute(sql, (id,))
                    print("Successfully Deleted...")
                except Exception as e:
                    print("Oops! Something wrong")
                    print (e)
     
            connection.commit()
        finally:
            connection.close()
            

    print("1. Create\n2. Read\n3. Update\n4. Delete");

    choice=int(input("Enter Your Choice:   "))

    if choice==1:
        create()
    elif choice==2:
        print("List of Student: ")
        read()
    elif choice==3:
        
        update()
    elif choice==4:
        
        delete()
    else:
        print("Invalid Input");
main()

