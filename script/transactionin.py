import psycopg2

def getsurrender():
    constr = """
       dbname='edelmerdb'
       user='edelmer'
       password='edelmer123'
       host='pythonista.learning.edu'
    """
    conn = psycopg2.connect(constr)
    curr = conn.cursor()
    curr.execute("select * from surrendernew1")
    rows = curr.fetchall()
    return rows

def index(req):
    header = """
	<!DOCTYPE html>
	<html>
	<head>
	<title>Grifter's Rerntal System'</title>
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
        <h1>Movies Check In (Return Module)</h1>
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
    <th> Transaction ID </th>
    <th> Customer Lastname</th>
    <th> Customer Firstname</th>
    <th> Customer Middlename</th>
    <th> Movie Title</th>
    <th>Penalty</th>
    """
    tableend = "</table>"
    panelend = """
    </div>
    <table>
    <tr>
    <td><a href="http://pythonista.learning.edu/~edelmer/index.py" class="btn btn-info btn-sm active">Back</a><td>
    </table>
    """

    surrender= getsurrender()
    surrendercontents = ""
    i = 1
    for balik in surrender:
        if i % 2 == 0:
            class_ = 'class="warning"'
        else:
            class_=""

        surrendercontents += "<tr "+class_+">"
        surrendercontents += '<td>'+str(balik[0])+"</td>"
        surrendercontents += '<td>'+balik[1]+"</td>"
        surrendercontents += "<td>"+balik[2]+"</td>"
        surrendercontents += "<td>"+balik[3]+"</td>"
        surrendercontents += "<td>"+balik[4]+"</td>"
        surrendercontents += "<td>"+str(balik[5])+"</td>"
        surrendercontents += "</tr>"
        i = i + 1

    return header + bodybegin + panelbegin + tablebegin + surrendercontents + tableend + panelend + bodyend