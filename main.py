from flask import Flask, render_template
from algorithm.app import algorithm_bp

app = Flask(__name__)
app.register_blueprint(algorithm_bp, url_prefix='/algorithm')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5001")
