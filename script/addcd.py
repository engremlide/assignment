import psycopg2
import cgi

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

def index(req, cdno):
    cdno = cgi.escape(cdno)
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
        <h1>Grifter's 'Movie Rental Customer List</h1>
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
        <div class="panel-heading">Listing</div>
        <div class="panel-body">
        <form action = "savecd.py">
        <table border = "1">
        <tr>
        <td>CD No:</td>
        <td>Title:</td>
        <td>Year Release:</td>
        <td>Typedisk:</td>
        <td>Category:</td>
        <td>Main Cast:</td>
        <td>Price of the Movie:</td>
        <td>No of Days:</td>
        <td>Penalty:</td>
        </tr>
        <tr>
        <td> <input type='text' name='cdno'> </td>
        <td> <input type='text' name='title'> </td>
        <td> <input type='text' name='year_release'> </td>
        <td> <input type='text' name='typedisk'> </td>
        <td> <input type='text' name='category'> </td>
        <td> <input type='text' name='casting'> </td>
        <td> <input type='text' name='price'> </td>
        <td> <input type='text' name='no_of_days'> </td>
        <td> <input type='text' name='penalty'> </td>
        </tr>
        </table>
        <input type = 'submit' value = 'save' class="btn btn-info btn-sm active">
        <input type = 'reset' value = 'reset' class="btn btn-info btn-sm active">
        </form>
        """
    tablebegin = """<table class="table table-hover table-condensed">
    """
    tableend = "</table>"
    panelend = """<table>
    <tr>
    <td><a href="http://pythonista.learning.edu/~edelmer/index.py".class="btn btn-info btn-sm active">Back</a><td>
    </table>
       </div>
      </div>
    """


    return header + bodybegin + panelbegin + tablebegin + tableend + panelend + bodyend