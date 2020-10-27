import pymysql

conn = pymysql.connect(
    host='database-3.cmbrfvsl2dzj.us-east-1.rds.amazonaws.com',
    port=int(3306),
    user="admin",
    passwd="yashyash123",
    db="studentdemo")

print("connected");


#cursor=conn.cursor()
#create_table="""
#create table Details (name varchar(200),email varchar(200),contact decimal(10),address text)
#"""
#cursor.execute(create_table)#


def insert_details(name,email,contact,address):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (name,email,contact,address) VALUES (%s,%s,%s,%s)", (name,email,contact,address))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details

