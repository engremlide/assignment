import psycopg2

constr = """
    dbname='edelmerdb'
    user='edelmer'
    password='edelmer123'
    host='pythonista.learning.edu'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from borrownew1")
rows = curr.fetchall()

for row in rows:
    print "=====View Customer Summary===="
    print "Transaction Id:" + str(row[0])
    print "Customer Lastname:" + str(row[1])
    print "Customer Firstname:" + str(row[2])
    print "Customer Middlename:" + str(row[3])
    print "CD Title:" + str(row[4])
    print "Payment:" + str(row[5])
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO borrownew1
             (transactionid, clastname, cfirstname, cmiddlename, cdtitle, payment)
             VALUES (1,'llantos','orven','rakista', 'white house down',35 )""")
conn.commit()

curr.execute("""
             INSERT INTO borrownew1
             (transactionid, clastname, cfirstname, cmiddlename, cdtitle, payment)
             VALUES (2,'llantos','orven','rakista', 'oblivion',40 )""")
conn.commit()

curr.execute("""
             INSERT INTO borrownew1
             (transactionid, clastname, cfirstname, cmiddlename, cdtitle, payment)
             VALUES (3,'llantos','orven','rakista', 'world war z',50 )""")
conn.commit()

curr.execute("""
             INSERT INTO borrownew1
             (transactionid, clastname, cfirstname, cmiddlename, cdtitle, payment)
             VALUES (4,'pilongo','adonis maynard','balboa', 'white house down',35 )""")
conn.commit()

curr.execute("""
             INSERT INTO borrownew1
             (transactionid, clastname, cfirstname, cmiddlename, cdtitle, payment)
             VALUES (5,'pilongo','adonis maynard','balboa', 'oblivion',40 )""")
conn.commit()
