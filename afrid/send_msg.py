"""

------------DOCUMENTATION-------------
COPYRIGHT © SHAIK AFRID 2023
PYTHON CODE TO SEND MSG FROM HTML CODE
EMBEDED HTML CODE INTO PYTHON
---------------------------------------
"""
from username import username
from password import password
from twilio.rest import Client
class main_twilio:
    def __init__(number):
        global main_number
        main_number = number

    def order_id(no_order,amount_id):
        global orderid
        global amount_main
        #take from html file
        orderid = no_order
        amount_main = amount_id
    def message_creation():
        global message
        logo = ""
        order_id = orderid
        amount = amount_main
        link = "web link"
        message = "TQ FOR VISITING" + " " + logo + "YOUR ORDER ID :"+ " " +order_id + "AMOUNT :" +amount + " "+link
    def main():
        account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        account_path = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        client = Client(account_sid,account_path);
        client.create.message(to =main_number,
                      from_= "+1227",
                      body=message)
class collect_data:
    def main():
        global main_username
        global main_password
        main_username = username
        main_password = password     
if "__init__" == "__main__":
    #take number from html file
    collect_data.main()
    num = int(input(""))
    def search():
        file = open("username.txt",'r')
        if(username in file):
            return 1
        else :
            return 0
    def search2():
        file2 = open("passwords.txt")
        if(password in file2):
            return 1
        else:
            return 0
    def check():
        if(search == 1):
            if(search2 == 1):
                return 2
            else:
                return 1
        else:
            return "0"
    def store_data(num):
        file3 = open("phone_number.txt","r")
        file3.read(num)
    check()
    main_twilio(num)