from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sumsq/<value1>/<value2>")
def sumsq(value1, value2):
    value1_sq = float(value1) ** 2
    value2_sq = float(value2) ** 2
    sum_of_sq = value1_sq + value2_sq
    return f"<p>Sum of 2 squares is {sum_of_sq}.<p>"

if __name__ == "__main__":
    app.run()