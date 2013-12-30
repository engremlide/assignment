import psycopg2

def index(req):
    header = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">

    <title>Justified Nav Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="bootstrap/css/justified-nav.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="bootstrap/css/justified-nav.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="bootstrap/js/html5shiv.js"></script>
      <script src="bootstrap/js/respond.min.js"></script>
    <![endif]-->

</head>
    """
    bodybegin = """
       <body>
    <div class="container">
      <div class="masthead">
        <ul class="nav nav-justified">
          <table cellpadding = 10 cellspacing = 10>
          <td class="active"><a href="http://pythonista.learning.edu/~edelmer/index.py">Home</a>
          <td><a href="http://pythonista.learning.edu/~edelmer/customer.py">Customer</a></td>
          <td><a href="http://pythonista.learning.edu/~edelmer/cd.py">Movie List</a></td>
          <td><a href="http://pythonista.learning.edu/~edelmer/transaction.py">Transaction</a></td>
          <td><a href="http://pythonista.learning.edu/~edelmer/about.py">About</a></td>
          <td><a href="http://pythonista.learning.edu/~edelmer/contact.py">Contact</a></td>
          </tr>
          </table>
        </ul>
      </div>

      <!-- Jumbotron -->
      <div class="jumbotron">
        <h1>Contact US!</h1>
        <p><h1>For Inquiries and Reservation!!!!</h1>
        <p class="lead"> Celphone No. : 09179479401 Globe .</p>
        <p class="lead"> Email Add : engremlide@yahoo.com.ph.</p>

      </div>

      <!-- Site footer -->
      <div class="footer">
        <p>&copy; GrifterTM Copy Right Reserved</p>
      </div>

    </div> <!-- /container -->
    """
    bodyend = """
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
        </body>
</html>
    """

    panelbegin = """
      <div class="panel panel-default">
      <!-- Default panel contents -->
      <div class="panel-heading">   </div>
      <div class="panel-body">
      """
    tablebegin = """<table class="table table-hover table-condensed">"""
    tableend = """</table>
    """
    panelend = """<table>
    <tr>
    <td><a href="http://pythonista.learning.edu/~edelmer/index.py".class="btn btn-info btn-sm active">Back</a><td>
    </table>

      </div>
      </div>
    """




    return header + bodybegin + panelbegin + tablebegin + tableend + panelend + bodyend