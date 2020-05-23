from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf6568ce1efc81ee23486441007a3af36"
# Your Auth Token from twilio.com/console
auth_token = "4e9c4568f0b4ca6799679cfde4e3c031"

client = Client(account_sid, auth_token)


# we need to load the list of students, get their phone numbers and send the messages

message = client.messages.create(
    to="+59165010070",
    from_="+18706863873",
    body="Buenos días, estimado estudiante decirle que tenemos examen  el día 20/08/20, a las horas 10:00AM hasta las 12:00PM, estudiar los temas 1,2, 3 gracias por su atención.")

print(message.sid)
