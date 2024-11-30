import subprocess

# Add Entries to the address book dictionary. Key = Name, Value = Pho>
addressbook = {
    "Name1" : "+xxxxxxxxxxxx",
    "Name2" : "+xxxxxxxxxxxx"
}

# Loop through the addressbook dictionary and send each number the me>
for name, phone in addressbook.items():
    # SMS Message Template (try to keep it within 150 characters)
    smsmessage = f"Hi {name}, tera phone number hai {phone}"

    # Use subprocess.run function to send SMS
    subprocess.run(["termux-sms-send", "-n", phone, smsmessage])

    # Print confirmation of each send
    print(f"Sent Message to {name} via {phone}")

# Print end of process message
print("Message sending complete")
