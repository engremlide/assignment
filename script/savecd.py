import psycopg2
import cgi

def addcd(cdno, title, year_release, typename, categoryname, castname, priceval, no_of_days, penaltyval):
    constr = """
       dbname='edelmerdb'
       user='edelmer'
       password='edelmer123'
       host='pythonista.learning.edu'
    """

    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("""INSERT INTO cd
             (cdno, title,year_release, typename, categoryname, castname,priceval, no_of_days, penaltyval)
             VALUES ('""" +str(cdno)+"','"+title+"','"+year_release+"','"+typename+"""',
                 '"""+categoryname+"','"+castname+"','"+str(priceval)+"""',
                 '"""+no_of_days+"','"+str(penaltyval)+"')")
    conn.commit()

def index(req, cdno, title,year_release,typedisk,category, casting, price, no_of_days, penalty):
    cdno       = cgi.escape(cdno)
    title      = cgi.escape(title)
    year_release  = cgi.escape(year_release)
    typedisk   = cgi.escape(typedisk)
    category   = cgi.escape(category)
    casting    = cgi.escape(casting)
    price      = cgi.escape(price)
    no_of_days = cgi.escape(no_of_days)
    penalty    = cgi.escape(penalty)
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
    <h1>Grifter's 'New Customer has been successfully added!!</h1>
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
        <a href="http://pythonista.learning.edu/~edelmer/customer.py" class="btn btn-info btn-sm active">Back to Customer List Module</a>
    """
    tableend = "</table>"
    panelend = """
       </div>
      </div>
    """

    result = addcd (cdno,title, year_release, typedisk, category, casting, price, no_of_days, penalty)
    result = '<div class = "container">'
    result +='<div >'
    result +='<h1> '+str(result[0])+'</h1></div></div>'

    return header + bodybegin + panelbegin + tablebegin + tableend + panelend + bodyend