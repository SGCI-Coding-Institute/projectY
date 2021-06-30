from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/map")
def mapit():
    return render_template("leaflet-example.html")

if __name__=='__main__':
    app.run(debug = True)


