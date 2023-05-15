from flask import Flask, request
import kafkaProducer as kp

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST' and request.json != None:
        print(f"Request is: {request.json}")
        kp.sendToQueue('Webhook',request.json)
        return "webhook received successfully"
    else:
        return "Something went wrong"

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
