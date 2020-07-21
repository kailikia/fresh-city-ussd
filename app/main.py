from config import re,app,request,make_response,render_template,db
from ussdClass import USSDModel

# # for validating an Email
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# # for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
#
# # Define a function for validating an Email
# def checkEmail(email):
#     if(re.search(regex,email)):
#         return True
#     else:
#         return False

@app.before_first_request
def createTables():
    db.create_all()

@app.route('/')
def index():
    ussdChannel = "*483*384#" # Your ussd channel from Africa's Talking
    return ussdChannel
    # return render_template('index.html', channel=ussdChannel)

@app.route('/records')
def all():
    return render_template("index.html", ussds = USSDModel.fetch_all())

@app.route('/ussd', methods=['POST'])
def ussdSession():

    sessionId   = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phoneNumber", None)
    text        = request.values.get("text", None)

    textArray    = text.split("*") if text else text
    userResponse = textArray[-1] if isinstance(textArray, list) else text

    print("text array:",textArray)

    print("user response:",userResponse)

    # Screens
    nameMenu = '''CON Welcome to FreshCity Kenya Farmers Registration.
    What is your name?
    '''
    # More menu screens ...

    countyMenu = '''CON Which county is your Farm located?
    '''

    locationMenu = '''CON Which village/location/street/road is your Farm located?
    '''

    farmMenu = '''CON What are your Farm Products, separated in comas (e.g Nduma,Bananas,...)?
    '''

    manyMenu = '''CON When will they be ready to sell (in days)?
    '''

    quantityMenu = '''CON What quantity will be ready (i.e 5 Ltrs, 20 Kgs,..)?
    '''

    successMenu = '''END Registration Successfully received.
    '''

    error = '''END An error occured.
    '''
    # More menu screens ...

    # Session logic
    if len(textArray) == 0:
        menu = nameMenu

    elif len(textArray) == 1:
        menu = countyMenu

    elif  len(textArray) == 2:
        menu = locationMenu

    elif  len(textArray) == 3:
        menu = farmMenu

    elif len(textArray) == 4:
        menu = manyMenu

    elif len(textArray) == 5:
        menu = quantityMenu

    elif  len(textArray) == 6:
        payment = USSDModel(sessionID=sessionId,phoneNumber=phoneNumber,name=textArray[0],county=textArray[1],location=textArray[2],products=textArray[3],ready=textArray[4],quantity=textArray[5])
        payment.create_record()
        menu = successMenu

    else:
        menu = error

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
