
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection


db = mysql.connector.connect(
    host="192.168.1.10",
    user="qa_user",
    password="Qa@12345",
    database="ros2_data"
)

cursor = db.cursor()

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    message = data.get("message")

    # Insert into DB
    sql = "INSERT INTO messages (message) VALUES (%s)"
    cursor.execute(sql, (message,))
    db.commit()

    return jsonify({"status": "stored", "message": message})

@app.route('/data', methods=['GET'])
def get_data():
    cursor.execute("SELECT * FROM messages")
    result = cursor.fetchall()

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# trigger test
# trigger test
