document.write(
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Contact Book</title>
	<link href="{{ url_for('static', filename='css/bootstrap.min.css') }}" rel="stylesheet">
	<link href="{{ url_for('static', filename='css/main.css') }}" rel="stylesheet">
  </head>
  <body>
	<nav class="navbar navbar-default">
	  <div class="container-fluid">
		<div class="navbar-header">
		  <p class="navbar-brand navbar-middler" >Contact Book</p>
		</div>
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
		  <ul class="nav navbar-nav navbar-right">
			  <li><a href="{{ url_for('contacts') }}">View contacts</a></li>
		  </ul>
		</div>
	  </div>
	</nav>
	<div class="container">
		{% with messages = get_flashed_messages(with_categories=true) %}
		  {% if messages %}
			{% for category, message in messages %}
			  <div>{{ message }}</div>
			{% endfor %}
		  {% endif %}
		{% endwith %}
	</div>

    <script src="{{ url_for('static', filename='js/jquery-3.2.1.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/bootstrap-confirmation.min.js') }}"></script>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>




  </body>
</html>

);