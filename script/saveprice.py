import psycopg2
import cgi

def addprice(priceval):
    constr = """
       dbname='edelmerdb'
       user='edelmer'
       password='edelmer123'
       host='pythonista.learning.edu'
    """

    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("""INSERT INTO price
             (priceval)
             VALUES ('""" +priceval+"')")
    conn.commit()

def index(req, priceval):
    priceval = cgi.escape(priceval)
    header = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Grifter's Customer </title>
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
    <h1>Grifter's 'Movie Price has been successfully added!!</h1>
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
        <a href="http://pythonista.learning.edu/~edelmer/index.py" class="btn btn-info btn-sm active">Home</a>
        <a href="http://pythonista.learning.edu/~edelmer/setting.py" class="btn btn-info btn-sm active">Back to Setting Module</a>
    """
    tableend = "</table>"
    panelend = """
       </div>
      </div>
    """

    result = addprice (priceval)
    result = '<div class = "container">'
    result +='<div >'
    result +='<h1> '+str(result[0])+'</h1></div></div>'

    return header + bodybegin + panelbegin + tablebegin + tableend + panelend + bodyend