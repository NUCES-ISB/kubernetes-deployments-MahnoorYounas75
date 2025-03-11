from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App is Running on Kubernetes!"

@app.route("/db")
def db_test():
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="myuser",
            password="mypassword",
            host="postgres-service", 
            port="5432"
        )
        return "Database Connection Successful!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
