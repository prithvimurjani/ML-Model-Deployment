from flask import Flask , render_template , request
import independentVariable

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def hello():
    if request.method == "POST":
        x_variable = request.form["x_value"]
        y_predicted = independentVariable.y_prediction(x_variable)
      # print(y_predicted)
        y_predicted_display = y_predicted
    return render_template("index.html",y_value_display = y_predicted_display)

'''
@app.route("/sub", methods = ['POST'])
def submit():
    # HTML -> .py
    if request.method == "POST":
        name = request.form["username"]

    #.py -> HTML
    return render_template("sub.html", n = name)
'''

if __name__ == "__main__":
    app.run(debug=True)