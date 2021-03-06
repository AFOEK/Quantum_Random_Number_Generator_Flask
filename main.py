from flask import *
from qiskit import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import io
import seaborn as sns
from os import path
import time
import matplotlib
import glob

__version__ = "0.1.0rc0.9"
matplotlib.use('Agg')
app = Flask(__name__)
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
    <div class="error rainbow">Did you already auto generate number ? It's seems little empty in here</div>
</body>
<footer>&copy; Felix "AF&Ouml;&Eacute;K" MONTALFU 2021 <br/> For <a class="link" title="Help usage" href="help">Help</a></footer>
</html>
"""

@app.route('/auto_gen', methods=['GET', 'POST'])
def autogen():
    if request.method == 'POST':
        iteration = int(request.form["iteration"])
        shot = int(request.form["shots"])
        qubit = int(request.form["qubit"])
        auto_iter = int(request.form["auto_iter"])
        autogen.option = request.form["radio_chart"]
        freq={}
        rslt_list=[]
        for j in range (0,auto_iter):
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
            rslt_list.append(rslt)
        for numbers in rslt_list:
            if numbers in freq:
                freq[numbers] += 1
            else:
                freq[numbers] = 1
        autogen.data_frames = pd.DataFrame(list(freq.items()), columns=['Number', 'Frequency'])
    return "ok",200


@app.route('/', methods=['GET', 'POST'])
def main(results=None):
    if request.method == 'POST':
        iteration = int(request.form["iteration"])
        shot = int(request.form["shots"])
        qubit = int(request.form["qubit"])
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
        hex_digit = hex(rslt)
        oct_digit = oct(rslt) 
        if option == "rslt":
            return render_template("main.html", results=rslt)
        elif option == "bin":
            return render_template("main.html", results=bit_string)
        elif option == "digit":
            return render_template("main.html", results=digit)
        elif option == "hex":
            return render_template("main.html", results=hex_digit)
        elif option == "oct":
            return render_template("main.html", results=oct_digit)
        elif option == "all":
            final = digit + "\n" + str(rslt) + "\n" + bit_string + "\n" + hex_digit + "\n" + oct_digit
            return render_template("main.html", results=final)
    return render_template("main.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/stat', methods=['GET','POST'])
def stat(img=None):
    try:
        data_frame = autogen.data_frames
    except UnboundLocalError:
        if((data_frame == "") or (data_frame.empty)):
            return temp_string, 418
    except Exception:
        return temp_string, 418
    
    img_path = ""
    try:
        os.remove("static/image/plot_bar.png")
        os.remove("static/image/plot_heatmap.png")
        os.remove("static/image/plot_scatter.png")
        os.remove("static/image/plot.png")
    except:
        print("File already cleared")
        pass
    
    img_path_bar = os.path.join("static", "image", "plot_bar.png")
    img_path_scatter = os.path.join("static", "image", "plot_scatter.png")
    img_path_heatmap = os.path.join("static", "image", "plot_heatmap.png")

    if (request.method == 'POST'):
        opt = request.form["radio_chart"]
        if opt == "bar":
            figure = Figure(figsize=(6,6), dpi=110)
            ax = figure.subplots()
            output = io.BytesIO()
            autogen.data_frames.plot(x="Number", y="Frequency", kind="bar", legend=True, ax=ax)
            ax.set_title("Frequency distribution among generated random number")
            figure.savefig(img_path_bar)
        elif opt == "scatter":
            figure = Figure(figsize=(6,6), dpi=110)
            ax = figure.subplots()
            output = io.BytesIO()
            autogen.data_frames.plot(x="Number", y="Frequency", kind="scatter", legend=True, ax=ax)
            ax.set_title("Frequency distribution among generated random number")
            figure.savefig(img_path_scatter)
        elif opt == "heatmap":
            figure, ax = plt.subplots(figsize=(6,6), dpi=110)
            sns.heatmap(autogen.data_frames, cmap='YlGnBu', annot=True)
            figure.savefig(img_path_heatmap)
    timeout = 10
    attempt = 0
    while(glob.glob("static/image/*.png") or (attempt < timeout)):        
        if(path.isfile(img_path_bar)):
            img_path = img_path_bar
            break
        elif(path.isfile(img_path_heatmap)):
            img_path = img_path_heatmap
            break
        elif(path.isfile(img_path_scatter)):
            img_path = img_path_scatter
            break
        time.sleep(1)
        attempt += 1
    return render_template("stat.html", img=img_path)

if __name__ == "__main__":
    app.run(port=80, debug=True)
    #app.run()"Succesfully to generate data"