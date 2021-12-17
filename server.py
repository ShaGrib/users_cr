from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/read')


@app.route('/read')
def users():
    return render_template("readall.html", users=User.get_all())


@app.route('/new')
def new():
    return render_template("create.html")

@app.route('/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/read')


if __name__=="__main__":
    app.run(debug=True)