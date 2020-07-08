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
    mainMenu = '''CON Welcome to FreshCity Kenya. Choose an option below
    1. Register as a Farmer
    2. Register as a Collection Point Agent
    3. Buy Fresh Farm Produce
    4. Buy Kienyeji Produce
    5. Track your Order
    6. Contact Us Directly
    '''
    # More menu screens ...

    firstMenu = '''CON Enter your full name
    '''

    secondMenu = '''CON Shop at http://www.freschcity.co.ke
    '''

    thirdMenu = '''CON Call us on +254700 483348
    '''

    error = "END Invalid input"

    # Session logic
    if userResponse == '3'  or userResponse == '4' or userResponse == '5':
        menu = firstMenu

    elif userResponse == '1' or userResponse == '2':
        menu = secondMenu

    elif userResponse == '6':
        menu = thirdMenu

    elif userResponse == '':
        menu = mainMenu


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
