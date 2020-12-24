import mysql.connector


connection = mysql.connector.connect(host='192.168.10.10',
                                         database='djangodaily',
                                         user='djangodb',
                                         password='vfnvqhrvgQ')
cursor = connection.cursor()
cursor.execute("select super_parent_id, max(instance_id) as 'instance_id' from exams where super_parent_id != 0 and super_parent_id IS NOT NULL group by super_parent_id order by id, instance_id asc")
solution = cursor.fetchall()

for x in solution:
    print(x)

cursor.close()
connection.close()