import psycopg2

def getcustomer():
    constr = """
       dbname='edelmerdb'
       user='edelmer'
       password='edelmer123'
       host='pythonista.learning.edu'
    """

    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("select * from  customer ")
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
        <h1>Grifter's 'Movie Rental Customer List</h1>
        <table>
        <th
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
    tablebegin = """<table class="table table-hover table-condensed ">
    <th> Customer Lastname</th>
    <th> Customer Firstname</th>
    <th> Customer Middlename</th>
    <th> Customer Address</th>
    <th> Customer Gender</th>
    <th> Customer Contact No. </th>
    """
    tableend = "</table>"
    panelend = """<table>
    <tr>
    <td><a href="http://pythonista.learning.edu/~edelmer/addcustomer.py?customerid=" class="btn btn-info btn-sm active">Add New Customer</a><td>
    </table>
        </div>
        </div>
    """

    customer = getcustomer()
    tablecontents = ""
    i = 1
    for customers in customer:
        if i % 2 == 0:
            class_ = 'class="warning"'
        else:
            class_=""

        tablecontents += "<tr "+class_+">"
        tablecontents += '<td>'+customers[1]+"</td>"
        tablecontents += "<td>"+str(customers[2])+"</td>"
        tablecontents += "<td>"+customers[3]+"</td>"
        tablecontents += "<td>"+customers[4]+"</td>"
        tablecontents += "<td>"+customers[6]+"</td>"
        tablecontents += "<td>"+customers[7]+"</td>"
        tablecontents += "</tr>"
        i = i + 1


    return header + bodybegin + panelbegin + tablebegin + tablecontents + tableend + panelend + bodyend