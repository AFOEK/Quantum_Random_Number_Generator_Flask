from flask import *
from qiskit import *
import base64
from matplotlib.figure import Figure
import pandas as pd
import io

app = Flask(__name__)
data_frames = pd.DataFrame()
temp_string = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static\css\style.css">
    <link rel="shortcut icon" href="static\image\quantum.ico">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <title>Statistics</title>
</head>
<body>
    <div class="header">Statistics</div>
    <div class="error rainbow">Did you already auto generate data ? It's seems empty in here</div>
</body>
</html>
"""
@app.route('/', methods=['GET', 'POST'])
def main(results=None):
    if request.method == 'POST':
        iteration = int(request.form["iteration"])
        shot = int(request.form["shots"])
        qubit = int(request.form["qubit"])
        auto_iter = int(request.form["auto_iter"])
        option = request.form["radio_select"]
        circ = QuantumCircuit(qubit,qubit)
        if qubit==1:
            for i in range(0,qubit):
                circ.h(i)
                circ.measure(i,i)
        elif qubit==2:
            for i in range(0,qubit):
                circ.h(i)
                circ.measure(i,i)
        elif qubit==3:
            for i in range(0,qubit):
                circ.h(i)
                circ.measure(i,i)
        elif qubit==4:
            for i in range(0,qubit):
                circ.h(i)
                circ.measure(i,i)
        elif qubit==5:
            for i in range(0,qubit):
                circ.h(i)
                circ.measure(i,i)
        number = []
        for i in range(0, iteration):
            sim = Aer.get_backend('qasm_simulator')
            job = execute(circ, sim, shots=shot)
            result = job.result()
            count = result.get_counts(circ)
            max_prob = max(count, key=count.get)
            number.append(max_prob)
        strings = [str(number) for number in number]
        bit_string = "".join(strings)
        rslt = int(bit_string,2)
        digit = str(len(str(rslt)))
        if option == "rslt":
            return render_template("main.html", results=rslt)
        elif option == "bin":
            return render_template("main.html", results=bit_string)
        elif option == "digit":
            return render_template("main.html", results=digit)
        elif option == "all":
            final = digit + "\n" + str(rslt) + "\n" + bit_string
            return render_template("main.html", results=final)
    return render_template("main.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/stat', methods=['GET', 'POST'])
def stat(img=None):
    if not data_frames.empty:
        figure = Figure(figsize=(6,6), dpi=110)
        ax = figure.subplots()
        output = io.BytesIO()
        data_frames.plot(x="Number", y="Frequency", kind="bar", legend=True, ax=ax)
        ax.set_title("Frequency distribution among generated random number")
        figure.savefig(output, format="png")
        data = base64.b64encode(output.getbuffer()).decode("ascii")
        return render_template("stat.html", img=data)
    return temp_string

if __name__ == "__main__":
    app.debug = True
    app.run(port=80)