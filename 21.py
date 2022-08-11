from flask import Flask, request

# Create http server and run it
app = Flask("something")


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        return '<h1><div id="moshe"><li>mazda</li> <li>citroen</li> <li>chevrolet</li> <li>ferrari</li></div></h1>'
    elif request.method == 'POST':
        return "saved new car1"

@app.route('/')
def my_func():
    return "hello and welcome to the world of games11111111"


app.run(host="0.0.0.0", port=5001, debug=False)
