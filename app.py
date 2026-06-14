from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "API Is Working"

@app.route('/jobs')
def jobs():
    return jsonify([
        {"id": 1, "title": "Full Stack Developer"},
        {"id": 2, "title": ".NET Developer"}
    ])

@app.route('/apply', methods=['POST'])
def apply():
    data = request.get_json()

    return jsonify({
        "message": "Job Applied Successfully",
        "email": data["email"],
        "job_id": data["job_id"]
    })

if __name__ == '__main__':
    app.run(debug=True)