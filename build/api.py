from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Services Monitoring API!"

@app.route('/button1', methods=['GET'])
def button1():
    services = ["EMS","ash", "infra", "reminder", "EMS"]
    return jsonify(services)

@app.route('/button2', methods=['GET'])
def button2():
    servers = [f"Server {i + 1}" for i in range(13)]
    return jsonify(servers)

@app.route('/button3', methods=['GET'])
def button3():
    ems_servers = [f"ems {i + 1}" for i in range(6)]
    return jsonify(ems_servers)

@app.route('/button4', methods=['GET'])
def button4():
    services = ["ABB", "KUKA", "hshsTECHNO", "EMS"]
    return jsonify(services)

@app.route('/button5', methods=['GET'])
def button5():
    response = {"message": "Button 5 was clicked"}
    return jsonify(response)

@app.route('/button6', methods=['GET'])
def button6():
    response = {"message": "Button 6 was clicked"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
