#************************************************#
from flask import Flask, render_template
app= Flask(__name__)
#************************************************#
@app.route("/")
def index():
    return render_template("index.html", num=4,)
@app.route("/<x>")
def X(x):
    return render_template("index.html", num=int(x)//2, temp="yellow") 
#************************************************#
if __name__ == "__main__":
    app.run(debug= True)
#************************************************#