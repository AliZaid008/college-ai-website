from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = {
    "dean": "The dean of the college is Dr. Ahmed Ali.",
    "departments": "The college has Data Science, AI, and Robotics departments.",
    "location": "The college is located at University of Baghdad.",
    "hours": "The college opens from 8 AM to 2 PM."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"].lower()

    for key in data:
        if key in question:
            return jsonify({"answer": data[key]})

    return jsonify({"answer": "Sorry, I don't have information about that."})

if __name__ == "__main__":
    app.run(debug=True)