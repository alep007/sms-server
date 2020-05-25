from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "my_sid"
# Your Auth Token from twilio.com/console
auth_token = "my_token"

client = Client(account_sid, auth_token)


# we need to load the list of students, get their phone numbers and send the messages

message = client.messages.create(
    to="+59165010070",
    from_="+18706863873",
    body="Buenos días, estimado estudiante decirle que tenemos examen  el día 20/08/20, a las horas 10:00AM hasta las 12:00PM, estudiar los temas 1,2, 3 gracias por su atención.")

print(message.sid)
