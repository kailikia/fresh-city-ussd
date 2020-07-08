from flask import Flask, request, make_response, render_template
import random
import string


app = Flask(__name__)

@app.route('/')
def index():
    ussdChannel = "*483*384#" # Your ussd channel from Africa's Talking
    return ussdChannel
    # return render_template('index.html', channel=ussdChannel)

@app.route('/ussd', methods=['POST'])
def ussdSession():

    sessionId   = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phoneNumber", None)
    text        = request.values.get("text", None)

    textArray    = text.split("*") if text else text
    userResponse = textArray[-1] if isinstance(textArray, list) else text

    # Screens
    firstMenu = '''CON Welcome to FreshCity Kenya. Choose an option below
    1. Register as a Farmer
    2. Register as a Collection Point Agent
    3. Buy Fresh Farm Produce
    98. MORE
    '''
    secondMenu = '''CON Welcome to FreshCity Kenya. Choose an option below
    4. Buy Kienyeji Produce
    5. Track your Order
    6. Contact Us Directly
    0. BACK
    '''
    # More menu screens ...

    error     = "END Invalid input"

    # Session logic
    if userResponse == 0  or userResponse == '':
        menu = firstMenu
    elif userResponse == '98':
        menu = secondMenu
    #  More logic
    # '''
    # if userResponse == 1 :
    #     do something
    # if userResponse == 2 :
    #     do something else
    # ...
    # '''
    else:
        menu = error

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
