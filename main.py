from flask import *
from qiskit import *
import json

app = Flask(__name__)

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
        print(rslt)
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

@app.route('/stat')
def feedback():
    return render_template("stat.html")

if __name__ == "__main__":
    app.debug = True
    app.run(port=80)