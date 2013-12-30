import psycopg2
import cgi

def addcustomer(customerid,lastname, firstname, middlename, address, age, gender, mobile):
    constr = """
       dbname='edelmerdb'
       user='edelmer'
       password='edelmer123'
       host='pythonista.learning.edu'
    """

    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("""INSERT INTO customer
             (customerid, lastname,firstname, middlename, address, age, gender, mobile)
             VALUES ('"""""+str(customerid)',' lastname', 'firstname', 'middlename', 'address',' str(age)','gender', 'mobile')"""")
    conn.commit()
    return rows

def index(req, customerid, lastname,firstname,middlename,address, age, gender, mobile):
    customerid = cgi.escape(customerid, lastname, firstname, middlename,address,age,gender,mobile)
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
        <h1>Grifter's 'Movie Rental Add Customer</h1>
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
    <a href="http://pythonista.learning.edu/~edelmer/customer.py" class="btn btn-info btn-sm active">Save</a>
    <a href="http://pythonista.learning.edu/~edelmer/addcustomer.py?customerid=" class="btn btn-info btn-sm active">Cancel</a>
    """
    tableend = "</table>"
    panelend = """
       </div>
      </div>
    """

result = addcustomer(customerid,lastname, firstname, middlename, address, age, gender, mobile)
result = '<div class = "container">'
result += ''
result +=

    return header + bodybegin + panelbegin + tablebegin + tableend + panelend + bodyend