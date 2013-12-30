import psycopg2
import cgi

def getmovieinfo(movie):
    constr = """
       dbname='edelmerdb'
       user='edelmer'
       password='edelmer123'
       host='pythonista.learning.edu'
    """
    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("select * from cd where cdno = " + str(movie))
    rows = curr.fetchall()
    return rows[0]



def index(req, movie):
    movieid = cgi.escape(movie)
    header = """
	<!DOCTYPE html>
	<html>
	<head>
	<title>Grifter's Movies Database Example</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!-- Bootstrap -->
	<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">

	<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	<!--[if lt IE 9]>
	    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
	    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
	    <![endif]-->
	</head>
	    """
    bodybegin = """
       <body>
        <h1>Movie Details</h1>
    """
    bodyend = """
           <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
             <script src="https://code.jquery.com/jquery.js"></script>
           <!-- Include all compiled plugins (below), or include individual files as needed -->
           <script src="js/bootstrap.min.js"></script>
           <table>
           <tr>
           <td><a href="http://pythonista.learning.edu/~edelmer/cd.py".class="btn btn-info btn-sm active">Back</a><td>
           </table>

           </body>
           </html>
    """
    movie = getmovieinfo(movie)
    moviecontainer = '<div class="container"> '
    moviecontainer += ' <div class="starter-template"> '
    moviecontainer +=  ' <h1>Title: '+movie[1]+'</h1> '
    moviecontainer +=   '<p class="lead">Category:' +movie[4] + ' <br>'
    moviecontainer +=  'Release Year'+ str(movie[2])
    moviecontainer += '<br /> <a href="http://pythonista.learning.edu/~edelmer/index.py"'
    moviecontainer += 'class="btn btn-success btn-sm active">Main Page</a></p></div></div>'

    return header + bodybegin  + moviecontainer + bodyend
