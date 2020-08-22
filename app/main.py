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

    languageMenu = '''CON Choose a language
    1. Kiswahili
    2. English
    '''

    # Screens
    nameMenuEN = '''CON Welcome to FreshCity Kenya Farmers Registration.
    What is your name?
    '''

    nameMenuSW = '''CON Karibu kwenye Usajili wa Wakulima wa FreshCity Kenya.
    Jina lako ni nani?
    '''
    # More menu screens ...

    countyMenuEN = '''CON Which county is your Farm located?
    '''

    countyMenuSW = '''CON Shamba lako liko kaunti gani?
    '''

    locationMenuEN = '''CON Which village/location/street/road is your Farm located?
    '''

    locationMenuSW  = '''CON Shamba lako liko kitongoji gani?
    '''

    farmMenuEN = '''CON What products do you farm (e.g Nduma,Banana,Sukuma,...)?
    '''

    farmMenuSW = '''CON Unlima bidhaa gani (e.g Nduma,Ndizi,Sukuma,...)?
    '''

    manyMenuEN = '''CON When will they be ready to sell (in days)?
    '''

    manyMenuSW = '''CON Zitakuwa tayari siku gani (kwa mfano: Wiki mbili, miezi tatu..)?
    '''

    quantityMenuEN = '''CON What quantity will be ready (i.e 5 Ltrs, 20 Kgs,..)?
    '''

    quantityMenuSW = '''CON Kiasi gani kitakuwa tayari (kwa mfano: Lita 5 , Kilo 20 ,..)?
    '''

    successMenuSW = '''END Asanti sana, tumepokea usajili wako.
    '''

    successMenuEN = '''END Registration successfully received.
    '''

    error = '''END An error occured.
    '''

    # More menu screens ...
    # Session logic
    if len(textArray) == 0:
        menu = languageMenu

    elif len(textArray) == 1:
        if int(textArray[0]) == 2:
            menu = nameMenuEN
        else:
            menu = nameMenuSW

    elif len(textArray) == 2:
        if int(textArray[0]) == 2:
            menu = countyMenuEN
        else:
            menu = countyMenuSW

    elif len(textArray) == 3:
        if int(textArray[0]) == 2:
            menu = locationMenuEN
        else:
            menu = locationMenuSW

    elif len(textArray) == 4:
        if int(textArray[0]) == 2:
            menu = farmMenuEN
        else:
            menu = farmMenuSW

    elif len(textArray) == 5:
        if int(textArray[0]) == 2:
            menu = manyMenuEN
        else:
            menu = manyMenuSW

    elif len(textArray) == 6:
        if int(textArray[0]) == 2:
            menu = quantityMenuEN
        else:
            menu = quantityMenuSW

    elif  len(textArray) == 7:
        ussd = USSDModel(sessionID=sessionId,phoneNumber=phoneNumber,name=textArray[1],county=textArray[2],location=textArray[3],products=textArray[4],ready=textArray[5],quantity=textArray[6])
        ussd.create_record()
        if int(textArray[0]) == 2:
            menu = successMenuEN
        else:
            menu = successMenuSW

    else:
        menu = error

    resp = make_response(menu, 200)
    resp.headers["Content-type"] = "text/plain"
    return resp

if __name__ == "__main__":
    app.run(debug=True)
