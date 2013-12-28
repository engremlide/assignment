import psycopg2

constr = """
    dbname='movie_rent'
    user='postgres'
    password='123456'
    host='localhost'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from casting")
rows = curr.fetchall()

for row in rows:
    print "=====View Main Cast Summary===="
    print "Actor / Actress Fullname:" + row[0]
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO casting
             (castname)
             VALUES ('Anne Curtis')""")
conn.commit()

curr.execute("""
             INSERT INTO casting
             (castname)
             VALUES ('Vice Ganda')""")
conn.commit()