import psycopg2

constr = """
    dbname='movie_rent'
    user='postgres'
    password='123456'
    host='localhost'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from price")
rows = curr.fetchall()

for row in rows:
    print "=====View Prices Summary===="
    print "Amount:" + str(row[0])
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO price
             (priceval)
             VALUES (50)""")
conn.commit()

curr.execute("""
             INSERT INTO price
             (priceval)
             VALUES (65)""")
conn.commit()

curr.execute("""
             INSERT INTO price
             (priceval)
             VALUES (80)""")
conn.commit()

curr.execute("""
             INSERT INTO price
             (priceval)
             VALUES (95)""")
conn.commit()

curr.execute("""
             INSERT INTO price
             (priceval)
             VALUES (120)""")
conn.commit()