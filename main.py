from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/sumsq/<int:value1>/<int:value2>")
def sumsq(value1, value2):
    value1_sq = float(value1) ** 2
    value2_sq = float(value2) ** 2
    sum_of_sq = value1_sq + value2_sq
    return f"<p>Sum of 2 squares is {sum_of_sq}.</p>"

if __name__ == "__main__":
    app.run(debug=True)