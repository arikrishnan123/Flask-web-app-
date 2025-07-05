from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Hello from OCI DevOps CI/CD Pipeline with Rolling Deployment!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
