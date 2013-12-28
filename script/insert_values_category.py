import psycopg2

constr = """
    dbname='movie_rent'
    user='postgres'
    password='123456'
    host='localhost'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from category")
rows = curr.fetchall()

for row in rows:
    print "=====View Type of Film Category Summary===="
    print "Type:" + row[0]
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO category
             (categoryname)
             VALUES ('romance')""")
conn.commit()

curr.execute("""
             INSERT INTO category
             (categoryname)
             VALUES ('news')""")
conn.commit()
curr.execute("""
             INSERT INTO category
             (categoryname)
             VALUES ('mystery')""")
conn.commit()