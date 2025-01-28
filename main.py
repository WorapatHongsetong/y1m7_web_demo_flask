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
        colour = request.form.get('colour', type=str)

        if colour == "" or colour == None:
            colour = "#9adfe6"
        
        operations = []
        operations = request.form.getlist('operation')

        data = None

        if len(operations) == 1:
            if operations[0] == 'sin':
                data = ploter.sine(start, end)
            elif operations[0] == 'cos':
                data = ploter.cosine(start, end)
            elif operations[0] == 'tan':
                data = ploter.tangent(start, end)
            elif operations[0] == 'square':
                data = ploter.square(start, end)
            elif operations[0] == 'sqr':
                data = ploter.sqrt(start, end)
            if data:
                ploter.plot(data, c=colour)
        if len(operations) > 1:
            ploter.plot_s(operations, start, end, c=colour)

    return render_template('plotter.html', result=True)

if __name__ == "__main__":
    app.run(debug=True)