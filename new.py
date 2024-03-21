# This is a simple Python script to generate an HTML file

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>This is my Python-generated website.</p>
</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_content)
