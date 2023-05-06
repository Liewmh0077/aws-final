<!DOCTYPE html>
<html>
<head>
	<title>Delete Employee</title>
	<style>
		body {
			background-image: url("123.png");
			background-size: cover;
			background-repeat: no-repeat;
			background-attachment: fixed;
			font-family: Arial, sans-serif;
			margin: 0;
			padding: 0;
		}
		h1 {
			color: dodgerblue;
			text-align: center;
			font-size: 36px;
			margin-top: 50px;
		}
		form {
			margin: auto;
			max-width: 800px;
			padding: 20px;
			box-sizing: border-box;
			background-color: rgba(255, 255, 255, 0.9);
			border-radius: 10px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
		}
		label {
			display: block;
			font-size: 20px;
			font-weight: bold;
			margin-top: 20px;
		}
		button[type="submit"] {
			background-color: grey;
			color: white;
			padding: 10px 20px;
			font-size: 20px;
			border: none;
			border-radius: 5px;
			cursor: pointer;
			font-style: oblique;
			margin-top: 20px;
			transition: background-color .3s;
		}
		button[type="submit"]:hover {
			background-color: #444;
		}
	</style>
</head>
<body>
	<h1>Delete Employee</h1>
	<form action="/delete" autocomplete="on" method = "GET">
		<p>Employee with ID {{ id }} has been deleted.</p>
		<button type="submit" >Back to Home</button>
	</form>
</body>
</html>
