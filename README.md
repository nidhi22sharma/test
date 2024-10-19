from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy function to simulate status check
def check_status():
    # This is where you would place your actual logic
    # For example, fetching data from a database, etc.
    return "Status: All operations are running smoothly."

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # When the button is clicked, this code runs
        output = check_status()  # Call the status check function
        return render_template("home.html", output=output)  # Pass the status to the template

    return render_template("home.html")  # Render the page for GET requests without status

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1990)