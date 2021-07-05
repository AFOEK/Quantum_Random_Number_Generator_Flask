from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
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