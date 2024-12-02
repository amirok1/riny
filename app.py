from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='./')

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/uslugi")
def uslugi():
    return render_template("uslugi.html")

app.run("0.0.0.0", 80)