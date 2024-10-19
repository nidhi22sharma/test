<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Status Check</title>
</head>
<body>
    <h3>Check Status</h3>

    <!-- Form to trigger the status check via POST method -->
    <form action="/" method="POST">
        <button type="submit">Check Status</button>
    </form>

    <!-- Display the output only if it exists -->
    {% if output %}
        <h2>Result:</h2>
        <div>{{ output }}</div>
    {% endif %}
</body>
</html>