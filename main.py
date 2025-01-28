from flask import Flask, request
from flask import render_template
import ploter

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

@app.route("/plotter", methods=['GET', 'POST'])
def plotter():
    if request.method == 'POST':
        start = request.form.get('start', type=float)
        end = request.form.get('end', type=float)
        operation = request.form.get('operation')

        data = None
        if operation == 'sin':
            data = ploter.sine(start, end)
        elif operation == 'cos':
            data = ploter.cosine(start, end)
        elif operation == 'tan':
            data = ploter.tangent(start, end)
        elif operation == 'square':
            data = ploter.square(start, end)
        elif operation == 'sqr':
            data = ploter.sqrt(start, end)
        if data:
            ploter.plot(data)
        return render_template('plotter.html', result=True)
    return render_template('plotter.html', result=False)

if __name__ == "__main__":
    app.run(debug=True)