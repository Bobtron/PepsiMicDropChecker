from twilio.rest import Client

account_sid = 'AC4bc1fa78bf08c0219e61cf05022db524'
auth_token = '0438a8f9f285e2251a544c172aa5647d'
my_number = '+16692489371'
twilio_number = '+12202042030'


def textmyself(message):
    client = Client(account_sid, auth_token)
    # twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
    message = client.messages \
        .create(
            body=message,
            from_=twilio_number,
            to=my_number
        )


if __name__ == "__main__":
    textmyself("judaism")
