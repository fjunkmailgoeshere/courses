#!/usr/bin/python

import twilio

print twilio.__version__



from twilio.rest import TwilioRestClient


#live sid
account_sid = "AC0a5a1aaa79fde0c863e3684c2f5fd727" # Your Account SID from www.twilio.com/console
auth_token  = "a0630b41c151501adbe83a1fc7cb88f7"  # Your Auth Token from www.twilio.com/console

#test sid
#account_sid = "ACf3552ec1365221f29ee2289bbd1dbf55" # Your Account SID from www.twilio.com/console
#auth_token  = "6624145bb0a5c8c240b6bba6a60356b7"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="17209842370",    # Replace with your phone number
    from_="+17207705062") # Replace with your Twilio number

    #test number
    #from_="15005550006") # Replace with your Twilio number

print(message.sid)
