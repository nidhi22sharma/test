from flask import Flask, render_template, request, redirect, url_for
import script  # Import your external script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        group = request.form.get("group")
        type_ = request.form.get("type")
        mod = request.form.get("mod")
        
        output = script.execute(group, type_, mod)

        # Redirect to clear form data
        return redirect(url_for('home', output=output))
    
    output = request.args.get('output', "")
    return render_template("home.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
