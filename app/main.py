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
    nameMenu = '''CON Welcome to FreshCity Kenya Farmers Registration.
    What is your name?
    '''
    # More menu screens ...

    countyMenu = '''CON Which county is your farm located?
    '''

    farmMenu = '''CON What do you Farm, separated in comas (e.g Nduma,Bananas,...)?
    '''

    manyMenu = '''CON When will they be ready (in days)?
    '''

    successMenu = '''CON Registration Successfully received.
    '''

    error = '''CON An error occured.
    '''
    # More menu screens ...

    # Session logic
    if len(textArray) == 1:
        menu = nameMenu

    elif len(textArray) == 2:
        menu = countyMenu

    elif  len(textArray) == 3:
        menu = farmMenu

    elif len(textArray) == 4:
        menu = manyMenu

    elif  len(textArray) == 5:
        menu = successMenu

    else:
        menu = error

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
