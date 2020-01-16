from itertools import islice
from fbchat import Client
from fbchat.models import *

email = ''
password = ''

client = Client(email, password)

user = client.searchForUsers("")[0]

print("user ID: {}".format(user.uid))

for _ in range(50):
    client.send(Message(text="Test Bota"), thread_id=user.uid, thread_type=ThreadType.USER)

client.logout()
