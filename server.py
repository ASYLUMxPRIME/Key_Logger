# Run the following command to expose the Flask server to the internet using ngrok:
# 1. Install ngrok if you haven't already: https://ngrok.com/download
# Sign up for an account and get your auth token. it should be available on the signup dashboard.
# 2. Authenticate ngrok with your auth token:
# The command will automatically be set up for you on the dashboard.
#  ngrok authtoken YOUR_AUTH_TOKEN
# just ctrl C+V into you attacker terminal.
#  ngrok http 5000



from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_logs():
    logs = request.form.get('logs')
    print("[+] Logs received:")
    print(logs)
    return "OK", 200

if __name__ == '__main__':
    app.run(port=5000)

