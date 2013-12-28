import psycopg2

constr = """
    dbname='movie_rent'
    user='postgres'
    password='123456'
    host='localhost'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from typename")
rows = curr.fetchall()

for row in rows:
    print "=====View Type of Disk Summary===="
    print "Type:" + row[0]
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO typename
             (typenamedisk)
             VALUES ('vol')""")
conn.commit()
