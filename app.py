from datetime import datetime
from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from mailSending import send_Email
import json


with open("config.json","r") as c:
    params = json.load(c)["params"]

print(params)
app = Flask(__name__)

send_Email(params["user"],params["passwd"],"abhisheksagar513@gmail.com","This msg from Waoflix.")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable=False)
    content = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow())

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/",methods=["GET","POST"])
def indexPage():
    if request.method == "POST":
        todo = Todo(title=request.form["title"],content=request.form["content"])
        db.session.add(todo)
        db.session.commit()
        
    alltodo = Todo.query.all()
    return render_template("index.html",title="Home",alltodo=alltodo)

@app.route("/products")
def showMovies():
    return render_template("index.html",title="Movies")



if __name__ == "__main__":
    app.run(debug=True,port=8000)