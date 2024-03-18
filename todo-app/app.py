from flask import Flask, render_template, request, url_for, redirect
from database import connect_to_db, get_db

app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def index():
    db = get_db()
    tasks_getter = db.execute("select * from todolist")
    all_db_tasks = tasks_getter.fetchall()
    return render_template("index.html", all_db_tasks = all_db_tasks)


@app.route("/add_task", methods=["POST", "GET"])
def add_task():
    if request.method == "POST":
        user_task = request.form["user_task"]
        db = get_db()
        db.execute("insert into todolist (task) values (?)", [user_task])
        db.commit()
        return redirect(url_for("index"))

    return render_template("index.html")

@app.route("/delete_task/<int:id>", methods=["POST", "GET"])
def delete_task(id):
    if request.method == "GET":
        db = get_db()
        db.execute("delete from todolist where id = ?", [id])
        db.commit()
        return redirect(url_for("index"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
