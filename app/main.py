from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>DevOps Diploma Project</h1>
    <p>Application is running in Docker on Yandex Cloud!</p>
    <p>Infrastructure: Terraform</p>
    <p>Configuration: Ansible</p>
    <p>Containerization: Docker</p>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
