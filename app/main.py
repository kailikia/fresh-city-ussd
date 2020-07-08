from flask import Flask, request, make_response, render_template
import random
import string
import re

app = Flask(__name__)

# for validating an Email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

# Define a function for validating an Email
def checkEmail(email):
    if(re.search(regex,email)):
        return True
    else:
        return False

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
    mainMenu = '''CON Welcome to FreshCity Kenya
    1. Register as a Farmer
    2. Register as a Collection Agent
    3. Buy Fresh Produce
    4. Buy Kienyeji Produce
    5. Track your Order
    6. Contact Us Directly
    '''
    # More menu screens ...

    firstMenu = '''CON Shop at http://www.freschcity.co.ke
    '''

    secondMenu = '''CON Enter your Email
    '''

    thirdMenu = '''CON Call us on +254700 483348
    '''

    successMenu = '''CON Registration Successfully received.Type 0 to go to main menu
    '''

    error = '''CON An error occured.
    1. Register as a Farmer
    2. Register as a Collection Agent
    3. Buy Fresh Produce
    4. Buy Kienyeji Produce
    5. Track your Order
    6. Contact Us Directly
    '''
    # More menu screens ...

    # Session logic
    if userResponse == '3'  or userResponse == '4' or userResponse == '5':
        menu = firstMenu

    elif userResponse == '1' or userResponse == '2':
        menu = secondMenu

    elif userResponse == '6':
        menu = thirdMenu

    elif userResponse == '':
        menu = mainMenu

    elif checkEmail(userResponse):
        menu = successMenu

    else:
        menu = error

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
