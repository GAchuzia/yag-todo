from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_task')
def add_task():
    if request.method == "POST":
        user_task = request.form['user_task']
        
    return render_template("index.html", methods=["POST","GET"])

if __name__ == '__main__':
    app.run(debug = True)