import psycopg2

constr = """
    dbname='movie_rent'
    user='postgres'
    password='123456'
    host='localhost'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from customer")
rows = curr.fetchall()

for row in rows:
    print "=====View Customer Summary===="
    print "Customer ID:" + str(row[0])
    print "Lastname:" + row[1]
    print "Firstname:" + row[2]
    print "Middlename:" + row[3]
    print "Address:" + row[4]
    print "Age:" + str(row[5])
    print "Gender:" + row[6]
    print "Mobile:" + row[7]
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO customer
             (customerid, lastname,firstname, middlename, address, age,
             gender, mobile)
             VALUES (5,'balbutin', 'peach shanelle', 'iligan', 'lenienza',
                 1, 'female', '09192234321')""")
conn.commit()
