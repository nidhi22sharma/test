<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Status Checker</title>
</head>
<body>
    <h1>Check Status</h1>

    <form action="/" method="POST">
        <!-- Button to trigger the status check -->
        <button type="submit">Check Status</button>
    </form>

    <!-- Display the output -->
    {% if output %}
        <h2>Result:</h2>
        <div>{{ output }}</div>
    {% endif %}

</body>
</html>