import psycopg2

constr = """
    dbname='movie_rent'
    user='postgres'
    password='123456'
    host='localhost'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from no_of_days")
rows = curr.fetchall()

for row in rows:
    print "=====View No of Days Summary===="
    print "No of Days:" + str(row[0])
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO no_of_days
             (days)
             VALUES (7)""")
conn.commit()
curr.execute("""
             INSERT INTO no_of_days
             (days)
             VALUES (8)""")
conn.commit()
curr.execute("""
             INSERT INTO no_of_days
             (days)
             VALUES (9)""")
conn.commit()
