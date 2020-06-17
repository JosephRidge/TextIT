from twilio.rest import Client
client = Client(
    # "AC7b87bf4905744ead992b86e795cb1d8d",
    # "4a14c6e1d7007afcd9a5bceedc7dffae"

    "AC7a5f25dee65d13e18c63a772b49b1f57",
    "6868558833ac770ec4e1aecc71958163"
)



for msg in client.messages.list():
    print(f"{msg.body}")
  

# msg = client.messages.create(
#     to="+254729523545",
#     from_="+12057827759",
#     body="Hello from python script"
# )
# f sstring allows us to print docs that are in scope

# print(f"Created a new message: {msg.sid}")


