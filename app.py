# app.py
# 3.1 Servers and APIs - Flask server challenge

# Create a Flask web application with one route:
# /current_time/ -> Should respond with an HTML <p> tag containing the current time, in 24-hour format.
# For example, if it is 2pm right now, your website should read: <p>14:00</p>

from flask import Flask
from datetime import datetime

# create flask app
app = Flask(__name__)

# Your code here

# decorator to connect URL to function: to get current time (in 24hr format)
@app.route("/current_time/")
def current_time():
    current_time = datetime.now().strftime("%H:%M")
    return f"<p>{current_time}</p>"
    # current_time_str = current_time.strftime("%H:%M")
    # return f"<p>{current_time_str}</p>"

if __name__ == "__main__":
    app.run(debug=True)
