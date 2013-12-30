import psycopg2

def getmovies():
    constr = """
       dbname='edelmerdb'
       user='edelmer'
       password='edelmer123'
       host='pythonista.learning.edu'
    """

    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("select * from  cd ")
    rows = curr.fetchall()
    return rows

def index(req):
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
        <h1>Welcome to Grifter's 'Movies Database </h1>
    """
    bodyend = """
           <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
             <script src="https://code.jquery.com/jquery.js"></script>
           <!-- Include all compiled plugins (below), or include individual files as needed -->
           <script src="js/bootstrap.min.js"></script>
        </body>
</html>
    """

    panelbegin = """
    <div class="panel panel-default">
    <!-- Default panel contents -->
    <div class="panel-body">
    """
    tablebegin = """<table class="table table-hover table-condensed">
    <th> Title </th>
    <th> Year Release</th>
    <th>Disk Category</th>
    """
    tableend = "</table>"
    panelend = """<table>
    <tr>
    <td><a href="http://pythonista.learning.edu/~edelmer/addcd.py?cdno=" class="btn btn-info btn-sm active">Add New Movie</a><td>
    <td><a href="http://pythonista.learning.edu/~edelmer/index.py".class="btn btn-info btn-sm active">Back</a><td>
    </table>
       </div>
      </div>
    """

    movies = getmovies()
    tablecontents = ""
    i = 1
    for movie in movies:
        if i % 2 == 0:
            class_ = 'class="warning"'
        else:
            class_=""

        tablecontents += "<tr "+class_+">"
        tablecontents += '<td>'+movie[1]+"</td>"
        tablecontents += "<td>" +str(movie[2])+"</td>"
        tablecontents += "<td>" +movie[3]+"</td>"
        tablecontents += '<td><a href="http://pythonista.learning.edu/~edelmer/viewdetails?movie='+str(movie[0])+'" class="btn btn-info btn-sm active">Details</a></td>'
        tablecontents += "</tr>"
        i = i + 1


    return header + bodybegin + panelbegin + tablebegin + tablecontents + tableend + panelend + bodyend