from flask import *
from qiskit import *

app = Flask(__name__)
app.secret_key = "quantum computing are the future technology"

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        iteration = int(request.form.get("iteration"))
        shots = int(request.form.get("shots"))
        qubit = int(request.form.get("qubit"))
        auto_iter = int(request.form.get("auto_iter"))
        option = request.form["radio_select"]
        if option == "rslt":
            print()
        elif option == "bin":
            print()
        elif option == "digit":
            print()
        elif option == "all":
            print()
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