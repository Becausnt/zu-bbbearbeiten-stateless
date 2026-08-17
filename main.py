import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)
app.logger.setLevel('INFO')

@app.route("/")
def index():
    items = helper.get_all()
    app.logger.info(f"Rendering index with items: {items}")
    return render_template('index.html', items=items)


@app.route('/add', methods=["POST"])
def add():
    text = request.form.get("text")
    app.logger.info(f"Adding item: {text}")
    helper.add(text)
    return redirect(url_for("index"))


@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))