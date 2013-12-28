import psycopg2

constr = """
    dbname='movie_rent'
    user='postgres'
    password='123456'
    host='localhost'
    """

conn = psycopg2.connect(constr)
curr = conn.cursor()
curr.execute("select * from cd")
rows = curr.fetchall()

for row in rows:
    print "=====Movie Summary===="
    print "CD no:" + str(row[0])
    print "Cd Title:" + row[1]
    print "Release Year:" + str(row[2])
    print "Type of Disk:" + row[3]
    print "Category:" + row[4]
    print "Main Cast:" + row[5]
    print "Price:" + str(row[6])
    print "No of Days:" + str(row[7])
    print "Penalty:" + str(row[8])
    print "=====End Summary===="
    print " "

curr.execute("""
             INSERT INTO cd
             (cdno, title,year_release, typename, categoryname, castname,
             priceval, no_of_days, penaltyval)
             VALUES (4,'Percy Jackson', 2013, 'dvd', 'adventure',
                 'michael jackson', 35, 2, 20)""")
conn.commit()
