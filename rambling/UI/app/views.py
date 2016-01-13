from app import app

from flask import Flask, render_template, request, jsonify

containers = {}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/list_containers')
def list_containers():
    return jsonify(containers)


@app.route("/add_container", methods=['POST'])
def add_conatiner():
    if request.method == "POST":
        data = request.json
        if data:
            containers.update(data)
            return ("Pleasure doing business with you!")
        else:
            return("No JSON object!")
    else:
        return "HELLO WORLD"

