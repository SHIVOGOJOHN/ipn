from flask import Flask, request

app = Flask(__name__)

@app.route('/ipn', methods=['POST'])
def ipn_handler():
    # Capture the IPN request data
    data = request.json

    # Log or process the data
    print("Received IPN Notification:", data)

    # Verify the transaction data with PesaPal or perform any actions
    # Here you could update your database or send notifications

    return "IPN Received", 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
