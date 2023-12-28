from twilio.rest import Client

account_sid = "ACb86c90b1afa278e1ed0ac339eee1f12b"
auth_key = "7f4fdb92f643ad00afbb334a54ee2502"

class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_key)

    def send_message(self,message):

        message = self.client.messages \
            .create(
            body=message,
            from_="+12722228438",
            to='+97470355952'
        )
        print(message.status)