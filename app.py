from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # prepare your raw text
    text = "Hello DevOps!\nVersion: 10"
    # pass it into the template
    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
