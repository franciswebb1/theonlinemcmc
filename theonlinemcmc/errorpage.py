# output html page in case of errors

from theonlinemcmc import errormessages, emailresponse

def errorpage(erroroutput, errval, emailaddress, outdir):
  # the string containing the webpage
  htmlpage = """
<!DOCTYPE HTML>
<html>
<head>
  <!-- Theme Made By www.w3schools.com - No Copyright -->
<meta name="author" content="Matthew Pitkin">
<meta name="description" content="The Online MCMC">
<meta name="keywords" content="MCMC, Markov chain Monte Carlo, Bayesian, emcee, python, data analysis, probability">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<!-- Include theme font -->
<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">

<!-- Include jQuery -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!-- custom CSS file -->
<link rel="stylesheet" type="text/css" href="simple.css"/><title>The Online MCMC: Error page</title>

<!-- Include jQuery -->
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

<!-- custom CSS file -->
<link rel="stylesheet" type="text/css" href="../../simple.css"/>

<title>The Online MCMC: Error page</title>

<body>

<!-- Navbar -->
<nav class="navbar navbar-default">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="/">THE ONLINE MCMC</a>
    </div>
  </div>
</nav>

<div class="container-top bg-1 text-center">
  <h3 class="title">ERROR</h3>
  <p>
    <br><br>{errormessage}<br>
    <br><code>{erroroutput}</code><br><br>
  </p>
  <br>
  <br>
  <li><a href="pyfile.py"><code>pyfile.py</code></a> - the python file used to run the MCMC</li>
  <li><a href="mymodel.py"><code>mymodel.py</code></a> - the python model function</li>
</div>

 <footer class="container-fluid bg-2 text-center">
    <p class="footer"> <strong> &copy; Matthew Pitkin (2015). </strong>The code for this site is licensed under the <a style="color: #BD5D38" href="http://opensource.org/licenses/MIT">MIT license</a>. It is available on <a style="color: #BD5D38" href="https://github.com/mattpitkin/theonlinemcmc">github</a> and <a style="color: #BD5D38" href="https://bitbucket.org/mattpitkin/theonlinemcmc">bitbucket</a>.<br>This site is kindly hosted by the <a style="color: #BD5D38" href="http://www.gla.ac.uk/schools/physics/">School of Physics & Astronomy</a> at the <a style="color: #BD5D38" href="http://www.gla.ac.uk/">University of Glasgow</a>. They bear no reponsibility for the content of this site or the results that are produced.
    </p>

<!-- include Social Media sharing file -->
<?php
$shareurl = "http://www.theonlinemcmc.com";
include('../../social.inc');
?>
</div>
</body>
"""

  # the output php file
  errfile = 'index.php'
  fp = open(errfile, 'w')
  fp.write(htmlpage.format(errormessage=errormessages[errval],erroroutput=erroroutput))
  fp.close()
  
  # email the page
  emailresponse(emailaddress, outdir, runerror=True)
  