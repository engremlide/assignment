import psycopg2

constr = """
    dbname='movie_rent'
    user='postgres'
    password='123456'
    host='localhost'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from penalty")
rows = curr.fetchall()

for row in rows:
    print "=====View Penalty Summary===="
    print "Amount:" + str(row[0])
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO penalty
             (penaltyval)
             VALUES (120)""")
conn.commit()

curr.execute("""
             INSERT INTO penalty
             (penaltyval)
             VALUES (150)""")
conn.commit()
curr.execute("""
             INSERT INTO penalty
             (penaltyval)
             VALUES (200)""")
conn.commit()