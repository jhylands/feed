from flask import Flask, send_from_directory, render_template, Response
from app.item_manager import get_items
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html.j2", items=get_items())


@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)


@app.route("/javascript.js")
def get_js():
    acc = ""
    js_files = [os.path.join("static/js/", js_file) for js_file  in os.listdir("static/js") if js_file.endswith(".js")]
    for js_file in js_files:
        with open(js_file, "r") as f:
            acc += f.read()
    return Response(acc, mimetype='application/javascript')

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")
