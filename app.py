from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello():
    text = "Hello DevOps!\nVersion: 6"
    return Response(text, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
